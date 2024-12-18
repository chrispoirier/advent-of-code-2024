import sys
sys.path.append('../../')
from common.fileio import read_input
from equation import equation

# data = read_input("test.txt")
# data = read_input("test2.txt")
# data = read_input("test3.txt")
data = read_input("input.txt")
# print(data)

valid_eqs = []
for d in data:
    eq = equation(d)
    # print(eq.string())
    if eq.find_valid():
        valid_eqs.append(eq)
    else:
        print(str(eq.target) + ': ' + ' '.join(map(str, eq.numbers)))
        print('not found')

total = sum(eq.target for eq in valid_eqs)
print(total, "count: ", len(valid_eqs))