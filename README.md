# Perfect Calculator

This is a comprehensive calculator program written in Python that handles various mathematical operations with proper error handling and safety features.

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, division
- Advanced operations: power, square root, factorial
- Expression evaluation (e.g., "2 + 3 * 4", "5^2", "√16")
- Calculation history tracking
- Error handling for edge cases (division by zero, negative square roots, etc.)
- Safe expression evaluation to prevent code injection

## Usage

To run the calculator, execute the following command:

```bash
python calculator.py
```

The calculator provides an interactive menu with the following options:

1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Power (^)
6. Square Root (√)
7. Factorial (!)
8. Evaluate Expression
9. Show History
10. Clear History
0. Exit

## Examples

- Basic operations: Enter two numbers when prompted
- Expression evaluation: Enter expressions like "2 + 3 * 4" or "√16"
- Power: Calculate 2^3 by entering 2 as base and 3 as exponent
- Factorial: Calculate 5! by entering 5

## Safety Features

The calculator includes security measures to prevent malicious code execution when evaluating expressions. Only safe mathematical operations are allowed.

## Requirements

- Python 3.x