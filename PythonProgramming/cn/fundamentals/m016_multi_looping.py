# R = a + b
from sys import stdout

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]

# Show Header
stdout.write('|||')
for h in a:
    stdout.write(f'\t{h}')
print()
for d1 in a:
    stdout.write(f'|{d1}|')
    for d2 in b:
        R = d1 + d2
        stdout.write(f'\t{R}')
    print()