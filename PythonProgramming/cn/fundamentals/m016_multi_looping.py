# R = a + b
from sys import stdout

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]

# Show Header
stdout.write('|||')
for d1 in a:
    stdout.write(f'\t{d1}')

print()

# Show List
for d2 in b:
    stdout.write(f'|{d2}|')
    for d1 in a:
        R = d1 + d2
        stdout.write(f'\t{R}')
    print()