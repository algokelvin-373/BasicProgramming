from sys import stdout

def triangle_with_hole(line, length):
    for x1 in range(line):
        if line == length:
            stdout.write('*')
            continue
        if x1 == 0 or x1 == line - 1:
            stdout.write('*')
        else:
            stdout.write(' ')
    print()

def triangle_without_hole(line):
    for x1 in range(line):
        stdout.write('*')
    print()

def triangle():
    s = int(input('Input s: '))
    hole = input('With Hole (y/n): ')
    is_hole = (False, True)[hole == 'y']
    for line in range(1, s + 1):
        if is_hole:
            triangle_with_hole(line, s)
        else:
            triangle_without_hole(line)

def rectangle_with_hole(line, width, height):
    for w in range(width):
        if line == 0 or line == height - 1:
            stdout.write('*')
            continue
        if w == 0 or w == width - 1:
            stdout.write('*')
        else:
            stdout.write(' ')
    print()

def rectangle_without_hole(width):
    for w in range(width):
        stdout.write('*')
    print()

def rectangle():
    width = int(input('width: '))
    height = int(input('height: '))
    hole = input('With Hole (y/n): ')
    is_hole = (False, True)[hole == 'y']
    for h in range(height):
        if is_hole:
            rectangle_with_hole(h, width, height)
        else:
            rectangle_without_hole(width)

def diamond_without_hole(s):
    for x in range (s):
        for x1 in range(s-x-1):
            stdout.write(" ")
        for x2 in range(2*x+1):
            stdout.write("*")
        print()
    for x in range (s, 1, -1):
        for x1 in range(s-x+1):
            stdout.write(" ")
        for x2 in range(2*x-3):
            stdout.write("*")
        print()

def diamond_with_hole(s):
    for x in range (s):
        for x1 in range(s-x-1):
            stdout.write(" ")
        finish = 2*x+1
        for x2 in range(finish):
            if x2 == 0 or x2 == finish-1:
                stdout.write("*")
            else:
                stdout.write(" ")
        print()
    for x in range (s, 1, -1):
        for x1 in range(s-x+1):
            stdout.write(" ")
        finish = 2*x-3
        for x2 in range(finish):
            if x2 == 0 or x2 == finish-1:
                stdout.write("*")
            else:
                stdout.write(" ")
        print()

def diamond():
    s = int(input('Input s: '))
    hole = input('With Hole (y/n): ')
    is_hole = (False, True)[hole == 'y']
    if is_hole:
        diamond_with_hole(s)
    else:
        diamond_without_hole(s)

print('''
Type 2D:
1. Triangle
2. Rectangle
3. Diamond
''')
type_2d = input('Choose Type 2D: ')

match type_2d:
    case '1': triangle()
    case '2': rectangle()
    case '3': diamond()
