# %% No idea - happiness in an array for 2 disjoint sets (slow)
def report_happiness_long(line1, line2, line3, line4):
    M, N = line1.split()
    arr = line2.split()
    A = line3.split()
    B = line4.split()

    happiness = 0 
    for i, item_i in enumerate(arr): 
        if item_i in A:
            happiness += 1
        elif item_i in B:
            happiness += -1
        else:
            pass
    return happiness

# %%   With numpy babe
import numpy as np
def report_happiness_np(line1, line2, line3, line4):
    M, N = line1.split()
    arr = line2.split()
    values, counts = np.unique(arr, return_counts = True)


    A = set(line3.split())
    B = set(line4.split())

    happiness = 0
    for i, item in enumerate(values):
        if item in A: happiness+=counts[i]
        if item in B: happiness-=counts[i]

    return happiness

# %% The fastest method!!!!!   Go for this in the tutorials
from collections import Counter
def report_happiness(line1, line2, line3, line4):
    M, N = line1.split()
    arr = line2.split()

    occurance_dict = Counter(arr)

    A = set(line3.split())
    B = set(line4.split())

    happiness = 0
    for key, value in occurance_dict.items():
        if key in A: happiness+=value
        if key in B: happiness-=value
        

    return happiness



if __name__ == '__main__':
    line1 = '3 2'
    line2 = '1 5 3'
    line3 = '3 1'
    line4 = '5 7'
    print(report_happiness(line1, line2, line3, line4))
