# %% swap case
from turtle import clear


def swap_case(s):
    swapped_string = ''
    for idx, itx in enumerate(s):
        if itx.islower():
            swapped_string += itx.upper()
        elif itx.isupper():
            swapped_string += itx.lower()
        else:
            swapped_string += itx
    return swapped_string


if __name__ == '__main__':
    print(swap_case('Hi BaByyY!'))






