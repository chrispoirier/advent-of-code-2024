def rotate_45_degrees(data):
    n = len(data)
    rotated = [[] for _ in range(2 * n - 1)]
    for i in range(n):
        for j in range(len(data[i])):
            rotated[i + j].append(data[i][j])
    return [''.join(line) for line in rotated]

def rotate_135_degrees(data):
    n = len(data)
    rotated = [[] for _ in range(2 * n - 1)]
    for i in range(n-1, -1, -1):
        for j in range(len(data[i])-1, -1, -1):
            rotated[n-1 - i + j].append(data[i][j])
    return [''.join(line) for line in rotated]

def print_grid(data):
    for line in data:
        print(''.join(line))