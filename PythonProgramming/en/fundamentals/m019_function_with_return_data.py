# function general
def get_begin():
    return "Python Programming"

# function with parameter
def get_name(name):
    return f"Your name is {name}"

print(get_begin())
data = input("Input your name: ")
print(get_name(data))