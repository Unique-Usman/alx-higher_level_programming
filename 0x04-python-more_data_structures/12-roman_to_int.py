#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string == None:
        return 0
    r_n = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
    }
    res = 0
    while roman_string:
        one = roman_string[0]
        two = 'I'
        if len(roman_string) >= 2:
            two = roman_string[1]
        if r_n[one] < r_n[two]:
            res += (r_n[two] - r_n[one])
            roman_string = roman_string[2:]
        else:
            res += r_n[one]
            roman_string = roman_string[1:]
    return res
