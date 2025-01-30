print("*** Looping Multi Level *****")
print("Make Triangle")
t = int(input("Input t = "))
a = 1
for x in range(0, t):
    for y in range(t, x+1, -1):
        print(" ", end='')
    for z in range(0, a):
        print("*", end='')
    a += 2
    print()
