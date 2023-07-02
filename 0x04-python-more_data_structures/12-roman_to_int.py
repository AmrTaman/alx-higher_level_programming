#!/usr/bin/python3


def roman_to_int(roman_string):
    num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = 0
    temp = ""
    if roman_string:
        for x in roman_string:
            if x in num:
                if ((x == "X" and temp == "I") or
                   (x == "V" and temp == "I") or
                   (x == "L" and temp == "X") or
                   (x == "C" and temp == "X") or
                   (x == "D" and temp == "C") or
                   (x == "M" and temp == "C")):
                    sum += (num[x] - (2*num[temp]))
                else:
                    sum += num[x]
            temp = x
    return (sum)
