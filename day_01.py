
def part1(nums):
    inc = 0
    dec = 0
    prev = 0
    for num in nums[1:]:
        if (num > prev):
            inc += 1  
        prev = num
    print("Part1 sum: ", inc)

def part2(nums):
    inc = 0
    dec = 0
    prev = 0
    for idx, num in enumerate(nums):
        if (idx + 2) <= (len(nums) - 1):
            val = num + nums[idx + 1] + nums[idx + 2]
            if (val > prev & prev != 0):
                inc += 1  
            prev = val
    print("Part2 sum: ", inc)


with open("inputs/01.txt") as _file:
    nums = [int(line) for line in _file]
    part1(nums)
    part2(nums)