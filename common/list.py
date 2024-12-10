def extract_numbers(strings, index):
    numbers = []
    for s in strings:
        numbers.append(int(s.split()[index]))
    return numbers

def split_numbers(strings):
    numbers = []
    for s in strings:
        numbers.append([int(x) for x in s.split()])
    return numbers