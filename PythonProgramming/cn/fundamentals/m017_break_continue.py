from sys import stdout

# Break
for data in range(1, 20):
    if data % 2 == 0 and data % 3 == 0:
        break
    else:
        stdout.write(f'{data} ')

print()

# Continue
for data in range(1, 20):
    if data % 2 == 0 and data % 3 == 0:
        continue
    else:
        stdout.write(f'{data} ')

print()