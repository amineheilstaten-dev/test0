#!/usr/bin/env python3
"""
Test script for the Perfect Calculator
"""

from calculator import Calculator

def test_calculator():
    """Test the calculator functions."""
    calc = Calculator()
    
    print("Testing Perfect Calculator...")
    print("="*40)
    
    # Test basic operations
    print("1. Testing basic operations:")
    print(f"   10 + 5 = {calc.add(10, 5)}")
    print(f"   10 - 3 = {calc.subtract(10, 3)}")
    print(f"   4 * 7 = {calc.multiply(4, 7)}")
    print(f"   15 / 3 = {calc.divide(15, 3)}")
    
    # Test edge cases
    print("\n2. Testing edge cases:")
    try:
        calc.divide(10, 0)
    except ZeroDivisionError as e:
        print(f"   Division by zero handled: {e}")
    
    try:
        calc.sqrt(-4)
    except ValueError as e:
        print(f"   Square root of negative number handled: {e}")
    
    # Test advanced operations
    print("\n3. Testing advanced operations:")
    print(f"   2 ^ 8 = {calc.power(2, 8)}")
    print(f"   √16 = {calc.sqrt(16)}")
    print(f"   5! = {calc.factorial(5)}")
    
    # Test expression evaluation
    print("\n4. Testing expression evaluation:")
    expressions = [
        "2 + 3 * 4",
        "10 / 2 + 3",
        "2^3 + 1",
        "√25",
        "5! / 10"
    ]
    
    for expr in expressions:
        try:
            result = calc.evaluate_expression(expr)
            print(f"   {expr} = {result}")
        except Exception as e:
            print(f"   {expr} -> Error: {e}")
    
    # Show history
    print("\n5. Calculation history:")
    history = calc.get_history()
    for i, calc_str in enumerate(history, 1):
        print(f"   {i}. {calc_str}")
    
    print(f"\nTotal calculations in history: {len(history)}")

if __name__ == "__main__":
    test_calculator()