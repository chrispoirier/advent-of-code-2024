import sys
sys.path.append('../../')
from common.fileio import read_input
from xmas import check_xmas

#data = read_input("test.txt")
data = read_input("input.txt")

data = [[char for char in line if char in {'X', 'M', 'A', 'S'}] for line in data]

xmas = 0
for i in range(1, len(data)-1):
    for j in range(1, len(data[i])-1):
        if data[i][j] == 'A' and check_xmas(data, i, j):
            xmas += 1
print(xmas)