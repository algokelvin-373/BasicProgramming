# Implement 'continue' at for

dt = ""
for x in range(1, 10):
    if x % 2 == 0 and x % 3 == 0:
        continue
    elif x % 2 == 0:
        dt += str(x)
print(dt)
