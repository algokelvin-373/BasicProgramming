from sys import stdout


def triangle_with_hole(lines, length):
    for x1 in range(lines):
        if lines == length:
            stdout.write('*')
            continue
        if x1 == 0 or x1 == lines - 1:
            stdout.write('*')
        else:
            stdout.write(' ')
    print()

s = int(input('输入: '))
for line in range(1, s + 1):
    triangle_with_hole(line, s)