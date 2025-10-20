from sys import stdout

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

s = int(input('Input s: '))
diamond_with_hole(s)