from sys import stdout

def rectangle_without_hole(width):
    for w in range(width):
        stdout.write('*')
    print()

width = int(input('width: '))
height = int(input('height: '))
for h in range(height):
    rectangle_without_hole(width)