from collections import Counter

from fractions import Fraction

import numpy as np

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

def find_cycle_index(n): # cycle index plynomial
    cycle_set = set()
    cycle_list = [tuple([1]*n)]
    cycle_set.update(cycle_list)

    while True:
        cycle_set_prev = set(cycle_set)
        for idx, cycle in enumerate(cycle_list):
            for idy in range(len(cycle)-1):
                tuple_to_add = tuple([0]*idy+[1]+[0]*(len(cycle)-idy-1))
                if cycle[-1] == 1: new_cycle = tuple(map(lambda x, y: x + y, cycle, tuple_to_add))[0:-1]
                cycle_set.add(tuple(sorted(new_cycle, reverse=True)))
            
        cycle_list = list(cycle_set.symmetric_difference(cycle_set_prev))

        if len(cycle_list) == 0: break
    
    return cycle_set

def calculate_set_J(cycle_set, N):
    set_J = set()
    for cycle in cycle_set:
        zeros = N*[0]
        counter = Counter(cycle)
        for key,value in counter.items():
            zeros[key-1] += value
        set_J.add(tuple(zeros))
    
    return set_J


def get_cycle_index_polynomials(set_J):
    cycle_poly_dict = dict()
    for j in set_J:
        weight = 1
        for k in range(len(j)):
            weight = weight*(((k+1)**j[k])*factorial(j[k]))
        cycle_poly_dict[j] = Fraction(1,weight)




    return cycle_poly_dict    


def calculate_unique_order(cycle_poly_dict, s):
    #N = len(cycle_poly_dict.keys()[0])
    #fact_N = math.factorial(N)
    num_of_unique_order = 0
    for key,value in cycle_poly_dict.items():
        num_of_unique_order += s**sum(key)*value
    
    
    return num_of_unique_order


def combine_cycle_index_polys(poly1, poly2):
    poly_comb = dict()
            

    for key1,value1 in poly1.items():

        for key2,value2 in poly2.items():
            ind_key1 = np.ndarray.tolist(np.where(np.array(key1)!=0)[0])
            ind_key2 = np.ndarray.tolist(np.where(np.array(key2)!=0)[0])

            comb = [0]*(len(key1)*len(key2))
            for id1 in ind_key1:
                for id2 in ind_key2:
                    p, q = id1+1, key1[id1]
                    x, y = id2+1, key2[id2]
                    comb[np.lcm(p,x)-1] +=  int(p*q*x*y/np.lcm(p,x))
                    
            key_comb = tuple(comb)
            value_comb = value1*value2
            try: poly_comb[key_comb] += value_comb
            except: poly_comb[key_comb] = value_comb

    return poly_comb


def solution(w, h, s):
    cycle_set = find_cycle_index(w)
    set_J = calculate_set_J(cycle_set, w)
    cycle_index_poly_w = get_cycle_index_polynomials(set_J)
    cycle_set = find_cycle_index(h)
    set_J = calculate_set_J(cycle_set, h)
    cycle_index_poly_h = get_cycle_index_polynomials(set_J)

    cycle_index_poly_comb = combine_cycle_index_polys(cycle_index_poly_w, cycle_index_poly_h)


    num_of_unique_order = calculate_unique_order(cycle_index_poly_comb,s)

    return str(num_of_unique_order)


import time
now = time.time()
print(solution(3,3,3))
print((time.time()-now) * 1000)



