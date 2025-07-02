print("Basic Type Data -> Int, Float, Complex Number")
a = 4   # Type Data Integer
print("Value a = ", a, ", type = ", type(a))

b = 5.6   # Type Data Float
print("Value b = ", b, ", type = ", type(b))

c = (3 + 2j)    # Type Data Complex Number
print("Value c = ", c, ", type = ", type(c))

print("\nType Data Integer Long Digit")
d = 123456789098765432101234567890
print("Value d = ", d, ", type = ", type(d))

print("\nType Data Float Long Digit")
e = 0.123456789098765432101234567890123456789
print("Value e = ", e, ", type = ", type(e))

print("\n\n##############################################################\n\n")

print("Basic Type Data -> String")
f = "Hello, I am Kelvin. I'm ready to learn Python Programming"
print("Value f = ", f, ", type = ", type(f))    # 'str' is String

# String version 1
g = "Hello, I am Kelvin. " \
    "I'm ready to learn Python " \
    "Programming"
print("Value g = ", g, ", type = ", type(g))

# String version 2
h = '''\nHello, I am Kelvin.
    I'm ready to learn Python
    Programming'''
print("Value h = ", h, ", type = ", type(h))

i = "Kelvin Tandrio"
print("Value i[2] = ", i[2], ", type = ", type(i[2]))
print("Value i[5-10] = ", i[5:10], ", type = ", type(i[5:10]))
i = "Excellent"
print(i)
