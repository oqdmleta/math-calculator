import math 
def calculate(num1, num2, operator): 
  if operator == "+": 
    result = num1 + num2 
  elif operator == "-": 
    result = num1 - num2 
  elif operator == "*": 
    result = num1 * num2 
  else: 
    result = num1 / num2 
  return result