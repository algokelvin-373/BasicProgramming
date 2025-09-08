from sys import stdout

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

w_data = int(input('width: '))
h_data = int(input('height: '))
for h in range(h_data):
    rectangle_with_hole(h, w_data, h_data)