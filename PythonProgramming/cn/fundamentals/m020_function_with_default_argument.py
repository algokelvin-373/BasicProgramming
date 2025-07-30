# without default argument
def my_name(name, age):
    print("Your name : ", name)
    print("Your age  : ", age)

# with default argument
def my_name_latin(name="My Name", age=0):
    print("Your name latin : ", name)
    print("Your age  : ", age)

my_name('Kelvin', 29)
my_name_latin()     # without argument
my_name_latin('Tan', 20)    # with argument