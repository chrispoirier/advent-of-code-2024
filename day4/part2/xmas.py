def check_xmas(data, i, j):
    return is_config_1(data, i, j) or is_config_2(data, i, j) or is_config_3(data, i, j) or is_config_4(data, i, j)

def is_config_1(data, i, j):
    return ((data[i-1][j-1] == 'M' and data[i+1][j+1] == 'S') and (data[i-1][j+1] == 'M' and data[i+1][j-1] == 'S'))

def is_config_2(data, i, j):
    return ((data[i-1][j-1] == 'S' and data[i+1][j+1] == 'M') and (data[i-1][j+1] == 'S' and data[i+1][j-1] == 'M'))

def is_config_3(data, i, j):
    return ((data[i-1][j-1] == 'M' and data[i-1][j+1] == 'S') and (data[i+1][j-1] == 'M' and data[i+1][j+1] == 'S'))

def is_config_4(data, i, j):
    return ((data[i-1][j-1] == 'S' and data[i-1][j+1] == 'M') and (data[i+1][j-1] == 'S' and data[i+1][j+1] == 'M'))