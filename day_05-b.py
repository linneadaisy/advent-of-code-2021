from numpy import *
import re

with open("inputs/05.txt") as _file:
    file_contents = _file.read()
    lines = file_contents.split("\n")

    h = 1000
    w = 1000
    Matrix = zeros((w, h))

    for line in lines:
        cord = line.split(' -> ')
        _from = [int(c) for c in cord[0].split(',')]
        _to = [int(c) for c in cord[1].split(',')]
        x1 = _from[0]
        x2 = _to[0]

        y1 = _from[1]
        y2 = _to[1]

        xDir = x1
        yDir = y1

        while xDir != x2 or yDir != y2:
            Matrix[yDir][xDir] += 1
            if (x1 > x2):
                xDir = xDir - 1
            if (x1 < x2):
                xDir = xDir + 1

            if (y1 > y2):
                yDir = yDir - 1
            if (y1 < y2):
                yDir = yDir + 1

        Matrix[yDir][xDir] += 1

    print(Matrix)
    print('Part2 sum:', count_nonzero(Matrix > 1))
