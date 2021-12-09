def part1():
    nums = [2, 3, 4, 7]
    sum = 0
    for line in lines:
        afterPipe = line.split('|')[1]
        for str in afterPipe.split():
            if len(str) in nums: sum += 1
    return sum


with open("inputs/08.txt") as _file:
    file_contents = _file.read()
    lines = file_contents.splitlines()

    print('Sum part1: ', part1())