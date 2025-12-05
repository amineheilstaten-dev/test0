#!/usr/bin/env python3
"""
Example usage of the Perfect Calculator
"""

from calculator import Calculator

def demo():
    """Demonstrate different ways to use the calculator."""
    calc = Calculator()
    
    print("Perfect Calculator Demo")
    print("="*30)
    
    # Example 1: Basic operations
    print("\n1. Basic Operations:")
    print(f"   Addition: 15 + 25 = {calc.add(15, 25)}")
    print(f"   Subtraction: 50 - 20 = {calc.subtract(50, 20)}")
    print(f"   Multiplication: 6 * 7 = {calc.multiply(6, 7)}")
    print(f"   Division: 100 / 4 = {calc.divide(100, 4)}")
    
    # Example 2: Advanced operations
    print("\n2. Advanced Operations:")
    print(f"   Power: 3^4 = {calc.power(3, 4)}")
    print(f"   Square Root: √144 = {calc.sqrt(144)}")
    print(f"   Factorial: 6! = {calc.factorial(6)}")
    
    # Example 3: Expression evaluation
    print("\n3. Expression Evaluation:")
    expressions = [
        "2 + 3 * 5",
        "(10 + 5) / 3",
        "2^10",
        "√64",
        "√(100 - 36)",
        "4! + 5*3"
    ]
    
    for expr in expressions:
        try:
            result = calc.evaluate_expression(expr)
            print(f"   {expr} = {result}")
        except Exception as e:
            print(f"   {expr} -> Error: {e}")
    
    # Example 4: Error handling
    print("\n4. Error Handling:")
    try:
        calc.divide(10, 0)
    except ZeroDivisionError as e:
        print(f"   Division by zero: {e}")
    
    try:
        calc.sqrt(-25)
    except ValueError as e:
        print(f"   Square root of negative: {e}")
    
    # Example 5: History
    print(f"\n5. Calculator History ({len(calc.get_history())} calculations):")
    for i, calc_str in enumerate(calc.get_history()[-5:], 1):  # Show last 5
        print(f"   {i}. {calc_str}")
    
    print("\nDemo completed successfully!")

if __name__ == "__main__":
    demo()