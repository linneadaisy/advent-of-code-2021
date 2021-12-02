horizontal  = 0
depth_part1  = 0
depth_part2  = 0
aim = 0

with open("inputs/02.txt") as _file:
    file_contents = _file.read()
    lines = file_contents.splitlines()
    for line in lines:
        arr = line.split()
        cmd = arr[0]
        value = int(arr[1])
        match cmd:
            case 'forward':
                horizontal += value
                depth_part2 += aim * value
            case 'down':
                depth_part1 += value
                aim += value
            case 'up':        
                depth_part1 -= value
                aim -= value

    print("Part1 sum: ", horizontal * depth_part1)
    print("Part2 sum: ", horizontal * depth_part2)