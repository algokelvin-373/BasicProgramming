import random
import string

letters = list(string.ascii_letters)  # ['a', 'b', ..., 'z', 'A', 'B', ..., 'Z']
numbers = list(string.digits)  # ['0', '1', ..., '9']
symbols = list(string.punctuation)  # ['!', '"', '#', ..., '~']

print(f"Welcome to Generator Password")
nr_letters = int(input('How many letters would you like in your password? '))
nr_symbols = int(input('How many symbols would you like? '))
nr_numbers = int(input('How many numbers would you like? '))

# Easy Level
password = ""
for char in range(1, nr_letters + 1):
    password += random.choice(letters)
for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)
for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)
print(password)