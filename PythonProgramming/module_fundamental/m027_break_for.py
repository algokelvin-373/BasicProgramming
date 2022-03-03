# Implement 'break' at looping

dt = ""
for x in range(1, 6):
    if x % 2 == 0 and x % 3 == 0:
        break
    elif x % 2 == 0:
        dt += str(x)
print(dt)
