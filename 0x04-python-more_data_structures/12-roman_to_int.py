#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    total = 0
    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for idx in range(len(roman_string)):
        i = rom_n.get(roman_string[idx])
        if (idx < len(roman_string) - 1):
            ii = rom_n.get(roman_string[idx + 1])
            if ii > i:
                total -= i
            else:
                total += i
        else:
            total += i
    return (total)
