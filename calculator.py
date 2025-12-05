#!/usr/bin/env python3
"""
A Perfect Calculator Program in Python

This calculator handles:
- Basic arithmetic operations (+, -, *, /)
- Advanced operations (power, square root, factorial, etc.)
- Error handling for edge cases
- Interactive mode and expression evaluation
"""

import math
import re
from typing import Union, List


class Calculator:
    """A comprehensive calculator class with various mathematical operations."""
    
    def __init__(self):
        """Initialize the calculator."""
        self.history = []
    
    def add(self, a: float, b: float) -> float:
        """Addition operation."""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """Subtraction operation."""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """Multiplication operation."""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: float, b: float) -> float:
        """Division operation with error handling."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def power(self, a: float, b: float) -> float:
        """Power operation (a^b)."""
        try:
            result = a ** b
            self.history.append(f"{a} ^ {b} = {result}")
            return result
        except OverflowError:
            raise OverflowError("Result is too large to calculate!")
    
    def sqrt(self, a: float) -> float:
        """Square root operation."""
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        result = math.sqrt(a)
        self.history.append(f"√{a} = {result}")
        return result
    
    def factorial(self, a: int) -> int:
        """Factorial operation."""
        if a < 0:
            raise ValueError("Cannot calculate factorial of negative number!")
        if a != int(a):
            raise ValueError("Factorial is only defined for integers!")
        result = math.factorial(int(a))
        self.history.append(f"{int(a)}! = {result}")
        return result
    
    def evaluate_expression(self, expression: str) -> float:
        """
        Safely evaluate a mathematical expression.
        
        Args:
            expression: A string containing a mathematical expression
            
        Returns:
            The result of the calculation
        """
        # Remove spaces
        expression = expression.replace(" ", "")
        
        # Validate the expression to prevent dangerous operations
        if not self._is_safe_expression(expression):
            raise ValueError("Invalid expression!")
        
        try:
            # Replace common math symbols with Python equivalents
            expression = expression.replace("^", "**")
            
            # Handle square root: replace √ followed by a number or expression in parentheses
            expression = re.sub(r"√(\d+(?:\.\d+)?)", r"math.sqrt(\1)", expression)  # √49
            expression = re.sub(r"√\(([^)]+)\)", r"math.sqrt(\1)", expression)      # √(25+10)
            
            # Handle some common functions
            expression = re.sub(r"(\d+)!", r"math.factorial(\1)", expression)
            
            # Evaluate the expression safely
            result = eval(expression, {"__builtins__": {}}, {
                "math": math,
                "abs": abs,
                "round": round,
                "pow": pow,
                "min": min,
                "max": max
            })
            
            self.history.append(f"{expression.replace('**', '^').replace('math.sqrt', '√')} = {result}")
            return result
        except Exception as e:
            raise ValueError(f"Error evaluating expression: {str(e)}")
    
    def _is_safe_expression(self, expression: str) -> bool:
        """
        Check if an expression is safe to evaluate.
        
        Args:
            expression: The expression to check
            
        Returns:
            True if safe, False otherwise
        """
        # Only allow numbers, operators, parentheses, and specific functions
        allowed_chars = set("0123456789+-*/().^√! ")
        
        # Check for allowed characters
        for char in expression:
            if char not in allowed_chars and not char.isalpha():
                return False
        
        # Check for potentially dangerous substrings
        dangerous_patterns = [
            "import", "exec", "eval", "__", "globals", "locals", 
            "open", "file", "system", "os", "subprocess"
        ]
        
        for pattern in dangerous_patterns:
            if pattern in expression.lower():
                return False
        
        return True
    
    def clear_history(self):
        """Clear the calculation history."""
        self.history = []
    
    def get_history(self) -> List[str]:
        """Get the calculation history."""
        return self.history.copy()


def print_menu():
    """Print the calculator menu."""
    print("\n" + "="*50)
    print("           PERFECT CALCULATOR")
    print("="*50)
    print("Operations:")
    print("  1. Addition (+)")
    print("  2. Subtraction (-)")
    print("  3. Multiplication (*)")
    print("  4. Division (/)")
    print("  5. Power (^)")
    print("  6. Square Root (√)")
    print("  7. Factorial (!)")
    print("  8. Evaluate Expression")
    print("  9. Show History")
    print("  10. Clear History")
    print("  0. Exit")
    print("="*50)


def get_number(prompt: str) -> float:
    """Get a number from user input with validation."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def main():
    """Main function to run the calculator."""
    calc = Calculator()
    
    print("Welcome to the Perfect Calculator!")
    
    while True:
        print_menu()
        
        try:
            choice = input("\nEnter your choice (0-10): ").strip()
            
            if choice == "0":
                print("Thank you for using the Perfect Calculator. Goodbye!")
                break
            
            elif choice == "1":
                # Addition
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.add(a, b)
                print(f"\nResult: {a} + {b} = {result}")
            
            elif choice == "2":
                # Subtraction
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.subtract(a, b)
                print(f"\nResult: {a} - {b} = {result}")
            
            elif choice == "3":
                # Multiplication
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.multiply(a, b)
                print(f"\nResult: {a} * {b} = {result}")
            
            elif choice == "4":
                # Division
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.divide(a, b)
                print(f"\nResult: {a} / {b} = {result}")
            
            elif choice == "5":
                # Power
                a = get_number("Enter base number: ")
                b = get_number("Enter exponent: ")
                result = calc.power(a, b)
                print(f"\nResult: {a} ^ {b} = {result}")
            
            elif choice == "6":
                # Square root
                a = get_number("Enter number: ")
                result = calc.sqrt(a)
                print(f"\nResult: √{a} = {result}")
            
            elif choice == "7":
                # Factorial
                a = get_number("Enter a non-negative integer: ")
                result = calc.factorial(a)
                print(f"\nResult: {int(a)}! = {result}")
            
            elif choice == "8":
                # Evaluate expression
                expr = input("Enter expression (e.g., '2 + 3 * 4', '5^2', '√16'): ")
                result = calc.evaluate_expression(expr)
                print(f"\nResult: {expr} = {result}")
            
            elif choice == "9":
                # Show history
                history = calc.get_history()
                if history:
                    print("\nCalculation History:")
                    for i, calc_str in enumerate(history, 1):
                        print(f"  {i}. {calc_str}")
                else:
                    print("\nNo calculations in history.")
            
            elif choice == "10":
                # Clear history
                calc.clear_history()
                print("\nHistory cleared.")
            
            else:
                print("\nInvalid choice! Please enter a number between 0 and 10.")
        
        except ZeroDivisionError as e:
            print(f"\nError: {e}")
        except ValueError as e:
            print(f"\nError: {e}")
        except OverflowError as e:
            print(f"\nError: {e}")
        except KeyboardInterrupt:
            print("\n\nCalculator interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\nUnexpected error: {e}")
        
        # Pause before showing menu again
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()