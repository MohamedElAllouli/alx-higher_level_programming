#!/usr/bin/python3
def roman_to_int(roman_string):
    valeur = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rest = 0
    i = 0

    if type(roman_string) is str and roman_string:
        for c in range(len(roman_string) - 1, -1, -1):
            if valeur[roman_string[c]] >= i:
                rest += valeur[roman_string[c]]
            else:
                rest -= valeur[roman_string[c]]
            i = valeur[roman_string[c]]
    return rest
