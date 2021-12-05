from numpy import *


def checkBingo(matrix):
    for i in range(matrix.shape[0]):
        if all(matrix[i] == matrix[i][0]):
            return True
    trans_arr = matrix.T

    for i in range(trans_arr.shape[0]):
        if all(trans_arr[i] == trans_arr[i][0]):
            return True
    return False


with open("inputs/04.txt") as _file:
    file_contents = _file.read()
    lines = file_contents.split("\n\n")
    numToCall = lines.pop(0).split(',')

    borads = []
    for idx, board in enumerate(lines):
        borad = []
        rows = board.split("\n")
        for row in rows:
            nums = row.split()
            borad.append(nums)
        borads.append(borad)

    npa = array(borads)

    for idx, num in enumerate(numToCall):
        #print('Call index: ', idx, ' num: ', num)
        for idx, b in enumerate(npa):
            b = where(b == num, 'X', b)
            npa[idx] = b
            match = checkBingo(b)
            if (match):
                winningBorad = array(b)
                b = unique(winningBorad)

                cleaned = [x for x in b.flatten() if x.isdigit()]
                nums = [int(c) for c in cleaned]

                tot = sum(nums)
                print(tot * int(num))
                exit()