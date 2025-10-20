# without default argument
def my_name(name, age):
    print(f'Name: {name}')
    print(f'Age : {age}')

# with default argument
def my_name_two(name='My Name', age=0):
    print(f'Name: {name}')
    print(f'Age : {age}')

print('Without default argument')
my_name('John', 20)

print()

print('With default argument')
print('1. Get default argument')
my_name_two()
print('2. With parameter data')
my_name_two('Tina', 21)