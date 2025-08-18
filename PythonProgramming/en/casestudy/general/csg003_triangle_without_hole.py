from sys import stdout


def triangle_without_hole(lines):
    for x1 in range(lines):
        stdout.write('*')
    print()

s = int(input('输入: '))
for line in range(1, s + 1):
    triangle_without_hole(line)