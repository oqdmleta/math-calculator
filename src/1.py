import math
def calculate(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
    else:
        raise ValueError('Unsupported operation')

# Test the code with a few inputs
print(calculate(5, 3, '+')) # Should print 8
print(calculate(10, 2, '-')) # Should print 8
print(calculate(6, 3, '*')) # Should print 18
print(calculate(12, 4, '/')) # Should print 3

