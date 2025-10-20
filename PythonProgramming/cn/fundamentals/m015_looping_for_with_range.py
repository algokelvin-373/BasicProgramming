from sys import stdout

# Range 1 until 6
for data in range(1, 6):
    stdout.write(f'{data} ')

print()

# Range 1 - 30 step by 5
for data in range(1, 30, 5):
    stdout.write(f'{data} ')