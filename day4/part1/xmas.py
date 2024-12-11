def check_xmas(data):
    xmas_count = 0
    str = ''
    for sublist in data:
        str += '|'+ ''.join(sublist)
    xmas_count += str.upper().count("XMAS")
    xmas_count += str.upper().count("SAMX")
    return xmas_count