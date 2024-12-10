def extract_numbers(strings, index):
    numbers = []
    for s in strings:
        numbers.append(int(s.split()[index]))
    return numbers