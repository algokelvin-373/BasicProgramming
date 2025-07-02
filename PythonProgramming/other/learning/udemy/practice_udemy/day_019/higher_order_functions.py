def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Implement Higher Order Functions
def calculator(n1, n2, func):
    return func(n1, n2)

num1 = 10
num2 = 5

result1 = calculator(num1, num2, add)
print(f"{num1} + {num2} = {result1}")

result2 = calculator(num1, num2, subtract)
print(f"{num1} - {num2} = {result2}")

result3 = calculator(num1, num2, multiply)
print(f"{num1} * {num2} = {result3}")

result4 = calculator(num1, num2, divide)
print(f"{num1} / {num2} = {result4}")