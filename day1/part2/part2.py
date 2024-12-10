import sys
sys.path.append('../../')
from common.fileio import read_input
from list import extract_numbers

#data = read_input("test.txt")
data = read_input("input.txt")
first = extract_numbers(data, 0)
second = extract_numbers(data, 1)

second_counts = {}
for s in second:
    if s in second_counts:
        second_counts[s] += 1
    else:
        second_counts[s] = 1

similarity = 0
for f in first:
    if f in second_counts:
        similarity += f * second_counts[f]

print(similarity)