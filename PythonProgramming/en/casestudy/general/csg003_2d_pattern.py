from sys import stdout

def create_hole(line, length):
    for x1 in range(line):
        if line == length:
            stdout.write('*')
            continue
        if x1 == 0 or x1 == line - 1:
            stdout.write('*')
        else:
            stdout.write(' ')
    print()

def without_hole(line):
    for x1 in range(line):
        stdout.write('*')
    print()

def triangle(count, with_hole):
    for line in range(1, count + 1):
        if with_hole:
            create_hole(line, count)
        else:
            without_hole(line)

print('''
Type 2D:
1. Triangle
2. Rectangle
3. Rhombus
''')
type_2d = input('Choose Type 2D: ')

n = int(input('Input n: '))
hole = input('With Hole (y/n): ')
isHole = (False, True)[hole == 'y']

triangle(n, isHole)
