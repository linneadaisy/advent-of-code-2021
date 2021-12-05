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
        y1 = _to[0]

        x2 = _to[1]
        y2 = _from[1]

        #part1
        if (x1 == y1):  #y
            start = min(x2, y2)
            stop = max(x2, y2)
            for i in range((stop + 1) - start):
                Matrix[start + i][x1] += 1

        if (x2 == y2):  #x
            start = min(x1, y1)
            stop = max(x1, y1)

            for i in range((stop + 1) - start):
                Matrix[y2][start + i] += 1

    print(Matrix)
    print('Part1 sum:', count_nonzero(Matrix > 1))
