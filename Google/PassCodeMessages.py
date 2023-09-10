# 1-) find the largest sum divisible to 3
from itertools import combinations
def remainder(input): return input % 3

def get_max_number(list_numbers):
    max_num = 0
    N = len(list_numbers)
    list_divisable = []
    for i in range(N,0,-1):
        comb = list(combinations(list_numbers,i))
        list_divisable_i = list(map(remainder, map(sum, comb)))
        if 0 in list_divisable_i:
            for j,item in enumerate(list_divisable_i):
                if item==0: list_divisable.append(comb[j])
            break

    max_num = 0
    for i in range(len(list_divisable)):
        max_str = map(str,sorted(list_divisable[i])[::-1])
        max_num_temp = int(''.join(max_str))
        if max_num_temp>max_num: max_num = max_num_temp
    return max_num
 

def solution(list_numbers):
    try: max_num = get_max_number(list_numbers)
    except: max_num = 0
    return max_num
