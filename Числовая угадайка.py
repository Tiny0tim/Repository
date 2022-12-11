from random import *


def is_valid(c):
    if c.isdigit():
        return True
    else:
        return False


def is_valid_num(c):
    if is_valid(c) is True:
        if 1 <= int(c) <= 100:
            return True
        else:
            return False


number = randint(1, 100)
print('Welcome to "guess the number game"!')

flag = False

while flag is False:
    c = input("Insert number ")
    if is_valid(c) is False:
        print('we need a number')
    if is_valid_num(c) is False:
        print("from 1 to 100")
    if is_valid_num(c) is True:
        cnum = int(c)
        if cnum < number:
            print('Your num is less than searched one')
        if cnum > number:
            print('your num is larger than searched one')
        if cnum == number:
            print('Your guess is correct!')
            flag = True
