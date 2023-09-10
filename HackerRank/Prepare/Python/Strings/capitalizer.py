# %%

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    count, ct, appended = [], 0, False
    for itx in s:    
        if itx == ' ':
            appended = False
            ct += 1
        else:
            if not appended:
                count.append(ct)
            appended = True
            ct = 0
    fullName = ''
    for idx, itx in enumerate(s.split()):
        fullName += ' '*count[idx] + itx.capitalize()

    return fullName


if __name__ == '__main__':
    s = 'hello       world  lol'
    print(solve(s))