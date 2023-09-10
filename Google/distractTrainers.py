# %% List solution
import time 
import numpy as np

def get_if_infinite_loop(item):
    item_sum = int((item[0]+item[1])/np.gcd(item[0],item[1]))
    # bitwise logic power of 2
    return bool(item_sum & (item_sum - 1))



def get_classified_dict(lst, lst_combinations):
    classified_dict = dict()
    for elem in set(lst):
        classified_dict[elem] = 0
        for list_item in lst_combinations:
            if (elem in list_item):
                ind = (list_item.index(elem)+1)%2

                classified_dict[elem] += lst.count(list_item[ind])
    
    classified_dict_sorted = sorted(classified_dict.items(), key=lambda pair: pair[1], reverse=False)

    return classified_dict_sorted

def all_pairs(lst):
    now = time.time()
    lst_combinations_all_TRUE = []
    sett = sorted(list(set(lst)))
    for idx in range(len(sett)-1):
        for idy in range(idx+1,len(sett)):
            it = (sett[idx], sett[idy])
            if_true = get_if_infinite_loop(it)
            if if_true: lst_combinations_all_TRUE.append(it)
    print(f'Elapsed time #1: {(time.time()-now)*1000}')

    #now = time.time()
    while True:
        matched_pair_found = False
        classified_dict_sorted = get_classified_dict(lst, lst_combinations_all_TRUE)
        for idx in range(len(classified_dict_sorted)-1):
            for idy in range(1,len(classified_dict_sorted)):
                pair = tuple(sorted([classified_dict_sorted[idx][0],classified_dict_sorted[idy][0]]))
                if pair in lst_combinations_all_TRUE: 
                    matched_pair = pair
                    matched_pair_found = True
                    break
            if matched_pair_found: break
        if matched_pair_found:
            lst.remove(matched_pair[0]) 
            lst.remove(matched_pair[1]) 
        else: break
        
    min_sum_workers = len(lst)
    #print(f'Elapsed time #2: {(time.time()-now)*1000}')


    return min_sum_workers


def solution(myList): # Banana games
    min_sum = all_pairs(myList)        
    return min_sum




input_list = [6, 2, 5, 2, 5, 9, 2, 7, 4, 5]

# input_list = [4, 4, 4, 4]
# input_list = [2,10, 5,6]
# input_list = [1,7]
# input_list = [1,7,3,21,13,19]
# input_list = [1,1,4,7,9]
# input_list = [3, 2]

now = time.time()
output = solution(input_list)
print(output)
print(f'Elapsed time {(time.time()-now)*1000}')










