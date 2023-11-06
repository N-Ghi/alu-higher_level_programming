#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for item in my_list:
        if item % 2 != 0:
           print(f'{item} is not divisible by 2')
        else:
           print(f'{item} is divisible by 2')
