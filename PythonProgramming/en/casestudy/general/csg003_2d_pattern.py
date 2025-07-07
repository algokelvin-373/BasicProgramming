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

print('''
Type 2D:
1. Triangle
2. Rectangle
3. Rhombus
''')
type_2d = input('Choose Type 2D: ')

match type_2d:
    case '1': triangle()



# n = int(input('Input n: '))

# width = int(input('width: '))
# height = int(input('height: '))
#
# hole = input('With Hole (y/n): ')
# isHole = (False, True)[hole == 'y']
#
# for h in range(height):
#     for w in range(width):
#         if h == 0 or h == height - 1:
#             stdout.write('*')
#             continue
#         if w == 0 or w == width - 1:
#             stdout.write('*')
#         else:
#             stdout.write(' ')
#     print()

# for h in range(height):
#     for w in range(width):
#         stdout.write('*')
#     print()

# triangle(n, isHole)
