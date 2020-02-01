#!/usr/bin/python3
import re
""" Pass the str to number """


def str_to_num(str_num):
    """ convert the string to a number """
    # Define the dict for the numbers
    numbers = {
        "zero": 0, "one": 1, "two": 2,
        "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8,
        "nine": 9, "ten": 10, "eleven": 11,
        "twelve": 12, "thirteen": 13, "fourteen": 14,
        "fifteen": 15, "sixteen": 16, "seventeen": 17,
        "eighteen": 18, "nineteen": 19, "twenty": 20,
        "thirty": 30, "forty": 40, "fifty": 50,
        "sixty": 60, "seventy": 70, "eighty": 80,
        "ninety": 90, "hundred": 100, "thousand": 1000,
        "million": 1000000, "billion": 1000000000
        }
    # Initializing variables to get str representetion for
    # B, M, T, H
    billion = ""
    million = ""
    thousand = ""
    hundred = ""
    # Initializing variables to put the result in integers
    total_infected = 0
    billion_nums = 1
    million_nums = 1
    thousand_nums = 1
    hundred_nums = 1
    # Regex to get the patterns in words
    pattern_billion = '(bi)...(on)'
    pattern_million = '(mi)...(on)'
    pattern_thousand = '(tho)..(and)'
    pattern_hundred = '(hu)...(ed)'

    # Capture the data in strings for
    # B, M, T, H
    if re.search(pattern_billion, str_num):
        res = re.search(pattern_billion, str_num)
        if res.span()[0] != 0:
            billion = str_num[:res.span()[1]]
            str_num = str_num[res.span()[1]:]
        else:
            pass
    
    if re.search(pattern_million, str_num):
        res = re.search(pattern_million, str_num)
        if res.span()[0] != 0:
            million = str_num[:res.span()[1]]
            str_num = str_num[res.span()[1]:]
        else:
            pass
    
    if re.search(pattern_thousand, str_num):
        res = re.search(pattern_thousand, str_num)
        if res.span()[0] != 0:
            thousand = str_num[:res.span()[1]]
            str_num = str_num[res.span()[1]:]
        else:
            pass
    
    if re.search(pattern_hundred, str_num):
        res = re.search(pattern_hundred, str_num)
        if res.span()[0] != 0:
            hundred = str_num[:res.span()[1]]
            str_num = str_num[res.span()[1]:]
        else:
            pass
    
    # Pass the string representation to number
    if not billion:
        billion_nums = 0
    else:
        billion_infected = [value for key, value in numbers.items() if key in billion]
        for infected in billion_infected:
            billion_nums *= infected
    
    if not million:
        million_nums = 0
    else:
        million_infected = [value for key, value in numbers.items() if key in million]
        for infected in million_infected:
            million_nums *= infected
    
    if not thousand:
        thousand_nums = 0
    else:
        thousand_infected = [value for key, value in numbers.items() if key in thousand]
        for infected in thousand_infected:
            thousand_nums *= infected

    if not hundred:
        hundred_nums = 0
    else:
        hundred_infected = [value for key, value in numbers.items() if key in hundred]
        for infected in hundred_infected:
            hundred_nums *= infected

    num_infected = [value for key, value in numbers.items() if key in str_num]
    for infected in num_infected:
            total_infected += infected
    
    # Get the total
    total_infected = total_infected + billion_nums + million_nums + thousand_nums + hundred_nums
    return total_infected