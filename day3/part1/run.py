import sys
sys.path.append('../../')
from common.fileio import read_input
import re

#data = read_input("test.txt")
data = read_input("input.txt")

data = ''.join(data)

pattern = re.compile(r"mul\(\d+,\d+\)")
matches = pattern.findall(data)

prodsum = 0
for i in range(len(matches)):
    matches[i] = matches[i].replace("mul(", "").replace(")", "").split(",")
    matches[i] = [int(x) for x in matches[i]]
    prodsum += matches[i][0] * matches[i][1]

print(prodsum)