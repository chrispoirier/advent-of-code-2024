import sys
sys.path.append('../../')
from common.fileio import read_input
from common.grid import rotate_45_degrees, rotate_135_degrees, print_grid
from xmas import check_xmas

#data = read_input("test.txt")
data = read_input("input.txt")

data = [[char for char in line if char in {'X', 'M', 'A', 'S'}] for line in data]

xmas = check_xmas(data)
#print(xmas)

transposed_data = [''.join(chars) for chars in zip(*data)]
xmas += check_xmas(transposed_data)
#print(xmas)

rotated_data = rotate_45_degrees(data)
xmas += check_xmas(rotated_data)
#print_grid(data)
#print_grid(rotated_data)
#print(xmas)

rotated_data = rotate_135_degrees(data)
xmas += check_xmas(rotated_data)
#print_grid(rotated_data)
print(xmas)