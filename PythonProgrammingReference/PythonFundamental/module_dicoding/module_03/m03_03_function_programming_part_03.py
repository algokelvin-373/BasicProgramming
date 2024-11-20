print("***** Argument Function *****")


# No using default argument
def get_name_data(name, age):
    print("Your name : ", name)
    print("Your age  : ", age)


# Using default argument
def get_name_data_02(name="Kelvin", age=23):
    print("Your name : ", name)
    print("Your age  : ", age)


# Get Error : Must define variable is not make default like 'get_name_data_04'
# def get_name_data_03(name="Kelvin", age):
#     print("Your name : ", name)
#     print("Your age  : ", age)


# Success
def get_name_data_04(name, age=23):
    print("Your name : ", name)
    print("Your age  : ", age)


print("Not using default argument")
get_name_data("Kelvin", 23)

print("\nUsing default argument")
get_name_data_02()
get_name_data_02(name="Angel", age=20)
get_name_data_02(age=18, name="Brigitta")
