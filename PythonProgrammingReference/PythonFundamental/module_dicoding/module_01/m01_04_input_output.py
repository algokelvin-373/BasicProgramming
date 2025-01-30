print("Basic Input Output")
data01 = input("Enter word: ")
data02 = input("Enter number: ")
print("Output type 1: ", data01)
print("Output type 2: %d" % int(data02))
print("Output type 3: %s and %d " % (data01, int(data02)))  # Must using 'int' to convert integer

print("\nInput Formula")
data03 = input("Input Your Math: ")
print("Result = ", eval(data03))