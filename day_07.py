import statistics
import math


def part1(median):
    sum = 0

    for pos in crabsPos:
        sum += abs(pos - median)

    print('Sum part1: ', int(sum))


def part2(mean, median):
    sum = 0

    r = round(mean)
    mean = math.floor(mean) if r > median else r

    for pos in crabsPos:
        diff = abs(pos - mean)
        for d in range(1, diff + 1, 1):
            sum += d

    print('Sum part2: ', sum)


with open("inputs/07.txt") as _file:
    file_contents = _file.read()
    crabsPos = [int(fc) for fc in file_contents.split(',')]

    mean = statistics.mean(crabsPos)
    median = statistics.median(crabsPos)

    part1(median)
    part2(mean, median)
