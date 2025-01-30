print("***** Looping WHILE *****")
print("Geometry Array")
a = int(input("Input a = "))
r = int(input("Input r = "))
n = int(input("Input n = "))
i = 0
while i <= n:
    Un = a*(r**i)
    print("Array ", i, "= ", Un)
    i += 1
