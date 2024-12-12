def read_input(file_name):
    with open(file_name, "r") as input:
        data = [line.strip() for line in input.readlines()]
    return data
