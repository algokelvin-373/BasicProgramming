print("Convert from Int to anything")
a = 1
print(a, "Convert to float = ", float(a))
print(a, "Convert to string = ", str(a))

print("\nConvert from Float to anything")
a = 1.2345
print(a, "Convert to int = ", int(a))
print(a, "Convert to string = ", str(a))

print("\nConvert from String (Float) to anything")
a = "32.5"
print(a, "Convert to float = ", float(a))
# print(a, "Convert to int = ", int(a)) --> Can not convert because string but type is float

print("\nConvert from String (Int) to anything")
a = "32"
print(a, "Convert to float = ", float(a))
print(a, "Convert to int = ", int(a))

print("\nConvert from String to anything")
a = "Python"
# print(a, "Convert to float = ", float(a)) -> Can not convert
# print(a, "Convert to int = ", int(a)) -> Can not convert
print(a, "Convert to list = ", list(a))

print("\nConvert from List to Set and Tuple")
a = [1, 2, 3, 2, 1, 4, 3, 5, 5, 6]
print(a, "Convert to Set = ", set(a))
print(a, "Convert to Tuple = ", tuple(a))

print("\nConvert from List couple to Dictionary")
a = [[1, 2], ['Programming', 'Python']]
print(a, "Convert to dictionary = ", dict(a))
