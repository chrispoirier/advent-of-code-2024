import sys
sys.path.append('../../')
from common.fileio import read_input
from common.list import extract_numbers

#data = read_input("test.txt")
data = read_input("input.txt")
first = extract_numbers(data, 0)
second = extract_numbers(data, 1)
first.sort()
second.sort()

diff = 0
for i in range(len(first)):
    diff += abs(first[i] - second[i])

print(diff)