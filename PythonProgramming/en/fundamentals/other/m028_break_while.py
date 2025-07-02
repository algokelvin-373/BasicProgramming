# Implement 'break' for while

x = 1
dt = ""
while x < 10:
    if x % 2 == 0 and x % 3 == 0:
        break
    elif x % 2 == 0:
        dt += str(x)
    x += 1
print(dt)
