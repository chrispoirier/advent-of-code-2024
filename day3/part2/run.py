import sys
sys.path.append('../../')
from common.fileio import read_input
import re

#data = read_input("test.txt")
data = read_input("input.txt")

data = ''.join(data)

pattern = re.compile(r"mul\(\d+,\d+\)|do\(\)|don't\(\)")
matches = pattern.findall(data)

do = True
prodsum = 0
for i in range(len(matches)):
    if matches[i] == "do()":
        do = True
    elif matches[i] == "don't()":
        do = False
    elif do:
        matches[i] = matches[i].replace("mul(", "").replace(")", "").split(",")
        matches[i] = [int(x) for x in matches[i]]
        prodsum += matches[i][0] * matches[i][1]

print(prodsum)