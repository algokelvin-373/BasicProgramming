# Implement 'continue' for while

x = 0
dt = ""
while x < 10:
    x += 1
    if x % 2 == 0 and x % 3 == 0:
        continue
    elif x % 2 == 0:
        dt += str(x)
print(dt)
