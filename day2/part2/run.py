import sys
sys.path.append('../../')
from common.fileio import read_input
from common.list import split_numbers
from safe import check_safe

#data = read_input("test.txt")
data = read_input("input.txt")
data = split_numbers(data)

safe = 0
for d in data:
    if check_safe(d):
        safe += 1
    else:
        for i in range(len(d)):
            temp = d[:i] + d[i+1:]
            if check_safe(temp):
                safe += 1
                break
        
print(safe)