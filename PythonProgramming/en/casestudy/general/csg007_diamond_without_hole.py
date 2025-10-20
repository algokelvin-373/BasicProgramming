from sys import stdout

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

s = int(input('Input s: '))
diamond_without_hole(s)