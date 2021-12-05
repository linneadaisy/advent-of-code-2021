import numpy as np

oxygen = ''
co2 = ''


def opposite(bit):
    return '0' if bit == '1' else '1'


def most_frequent(List):
    arr = np.array(List).astype(np.int64)
    counts = np.bincount(arr).argmin()
    return str(counts)


def get_index_positions(list_of_elems, element):
    index_pos_list = []
    for i in range(len(list_of_elems)):
        if list_of_elems[i] == element:
            index_pos_list.append(i)
    return index_pos_list


def calc(col, lines, test):
    tmp = []
    for line in lines:
        x = line[col]
        tmp.append(x)
    v = most_frequent(tmp)
    if test == 'ox':
        return get_index_positions(tmp, v)
    elif test == 'co2':
        return get_index_positions(tmp, opposite(v))


with open("inputs/03.txt") as _file:
    file_contents = _file.read()
    lines = file_contents.splitlines()
    oxygenLines = lines.copy()
    c02Lines = lines.copy()
    width = len(lines[0])

    for _ in range(width):
        if (len(oxygenLines) > 1):
            index_pos_list_ox = calc(_, oxygenLines, 'ox')
            for idx in reversed(index_pos_list_ox):
                del oxygenLines[idx]

        if (len(c02Lines) > 1):
            index_pos_list_c02 = calc(_, c02Lines, 'co2')
            for idx in reversed(index_pos_list_c02):
                del c02Lines[idx]

    for bit in oxygenLines[0]:
        oxygen += bit

    for bit in c02Lines[0]:
        co2 += bit

    print('oxygen: ', oxygen)
    print('co2: ', co2)
    print('Part2 sum: ', int(oxygen, 2) * int(co2, 2))
