gamma = ''
epsilon = ''

def most_frequent(List):
    return max(set(List), key = List.count)

def opposite(bit):
    return '0' if bit == '1' else '1'  

with open("inputs/03.txt") as _file:
    file_contents = _file.read()
    lines = file_contents.splitlines()
    dicts = {}

    for line in lines:
        for idx, char in enumerate(line):
            dicts.setdefault(idx, []).append(char)

    for key in dicts.keys():
        bit = most_frequent(dicts[key])
        gamma += bit
        epsilon += opposite(bit)

    print('Part1 sum: ', int(gamma, 2) * int(epsilon, 2))

