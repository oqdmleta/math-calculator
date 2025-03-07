  import math

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    else:
        return num1 / num2

print(calculate(5, 3, '+'))
print(calculate(7, 2, '-'))
print(calculate(9, 3, '*'))
print(calculate(18, 2, '/'))