from sys import stdout

for data in range(1, 10):
    if data % 2 == 0 and data % 3 == 0:
        break
    else:
        stdout.write(f'{data} ')

print()

for data in range(1, 10):
    if data % 2 == 0 and data % 3 == 0:
        continue
    else:
        stdout.write(f'{data} ')