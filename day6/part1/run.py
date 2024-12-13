import sys
sys.path.append('../../')
from common.fileio import read_input
from map import map

# data = read_input("test.txt")
data = read_input("input.txt")

mapObj = map(data)
print(mapObj.traverse())