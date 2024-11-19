# function general
def get_begin():
    print("Welcome in Python Programming")


# function with parameter
def get_name(name):
    print("Your name is ", name)


# function with return data
def get_result(formula):
    return "The result of ", formula, " is ", eval(formula)


get_begin()
data = input("Input your name: ")
get_name(data)
your_formula = input("Input your formula: ")
print(get_result(your_formula))
