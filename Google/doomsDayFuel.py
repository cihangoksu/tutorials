import time

import numpy as np
# %%
def solution(m):
    allzero, firstZero, reorder_needed = True, False, False
    num_terminal, sum_r = 0, 1
    sum_list = []
    source_indeces,terminal_indeces = [],[]
    for i, row in enumerate(m): 
        current_sum = sum(row)
        if current_sum==0:
            if i == 0: firstZero = True
            terminal_indeces.append(i)
            num_terminal += 1
        else: 
            allzero = False
            sum_r *= current_sum
            sum_list.append(current_sum)
            source_indeces.append(i)
            
    if firstZero: return [1]+(num_terminal-1)*[0]+[1]
    if allzero: return [1]+(len(m)-1)*[0]+[1]

    if terminal_indeces != list(range(len(m)-num_terminal,len(m))): reorder_needed = True

    num_transient = len(m)-num_terminal  
    
    P = np.matrix(m, dtype=float)
    Ps = P[source_indeces, :]
    
    # P = np.matrix(m, dtype=float)
    Ps = np.divide(Ps,np.transpose(np.tile(np.array(sum_list),[len(m),1])))

    Q = Ps[:,source_indeces]
    R = Ps[:,terminal_indeces]
        
    F =  np.linalg.inv(np.identity(num_transient)-Q)

    
    num_array = np.array(F[0,:]*R*sum_r/np.linalg.det(F))[0]
    
    num_array_rounded = num_array.round().astype(int) #for speed reasons

    num_array = np.array(num_array_rounded/np.gcd.reduce(num_array_rounded), dtype=int)
    
    result = np.ndarray.tolist(num_array) + [sum(num_array)]

    return result










#####################################
# Returns indexes of active & terminal states
def detect_states(matrix):
    active, terminal = [], []
    for rowN, row in enumerate(matrix):
        (active if sum(row) else terminal).append(rowN)
    return(active,terminal)

# Convert elements of array in simplest form
def simplest_form(B):
    B = B.round().astype(int).A1                   # np.matrix --> np.array
    gcd = np.gcd.reduce(B)
    B = np.append(B, B.sum())                      # append the common denom
    return np.ndarray.tolist((B / gcd).astype(int))

# Finds solution by calculating Absorbing probabilities
def solution2(m2):
    active, terminal = detect_states(m2)
    if 0 in terminal:                              # special case when s0 is terminal
        return [1] + [0]*len(terminal[1:]) + [1]
    m2 = np.matrix(m2, dtype=float)[active, :]       # list --> np.matrix (active states only)
    comm_denom = np.prod(m2.sum(1))                 # product of sum of all active rows (used later)
    P = m2 / m2.sum(1)                               # divide by sum of row to convert to probability matrix
    Q, R = P[:, active], P[:, terminal]            # separate Q & R
    I = np.identity(len(Q))
    N = (I - Q) ** (-1)                            # calc fundamental matrix
    B = N[0] * R * comm_denom / np.linalg.det(N)   # get absorbing probs & get them close to some integer
    return simplest_form(B)
#####################################














################## testing ##################
'''
PT =[[14.,  5.,  5.,  5.,  8.,  4., 14.,  9.,  9., 18.],
       [17., 18., 13.,  0., 16., 10.,  9., 15.,  4.,  0.],
       [17.,  3., 17., 16.,  3.,  5., 18.,  9.,  4., 14.],
       [10.,  1., 14., 14., 15., 17.,  7., 14., 12.,  5.],
       [17.,  3., 17., 11.,  1.,  0., 16., 16., 17., 11.],
       [ 3.,  2., 18.,  9., 13.,  6.,  2.,  5., 19.,  0.],
       [ 6., 14., 11., 14., 12.,  1., 10.,  8., 16.,  0.],
       [ 5.,  3.,  9.,  1.,  0., 11.,  4.,  0.,  0., 18.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.]]
assert solution(PT) == solution2(PT)
'''
'''
PT = [[17., 13., 15., 11.,  2., 13., 15.,  9.,  8.,  5.],
       [ 8., 17., 10., 13.,  4.,  6., 12., 18.,  1., 10.],
       [ 1., 19.,  8.,  4., 11., 10., 15., 16.,  2.,  0.],
       [ 7.,  3., 11.,  9., 15., 10., 12.,  2.,  1., 17.],
       [15., 14., 14., 10.,  3.,  0., 17.,  4.,  9.,  5.],
       [ 3.,  2., 16., 19., 19., 10.,  6.,  5., 15., 12.],
       [19., 19.,  6.,  9., 15., 17., 18.,  7., 16., 18.],
       [16.,  8.,  8., 12., 18.,  0.,  4., 18., 18.,  8.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.]]
'''
PT = [[ 7.,  1., 10.,  7.],
       [ 0.,  0.,  0.,  0.],
       [12., 15.,  1., 10.],
       [ 0.,  0.,  0.,  0.]]
# assert solution(PT) == solution2(PT)

now = time.time()
sol1 = solution(PT)
print(sol1)
print(f'passed = {time.time()-now}')
now = time.time()
sol2 =solution2(PT) 
print(sol2)
print(f'passed = {time.time()-now}')


import random

for i in range(990000):
    array_size = random.randint(1,10)
    term_size = random.randint(1,array_size)
    print([array_size, term_size])
    P = np.identity(array_size)
    for j in range(array_size):
        if j<(array_size-term_size): P[j,:] = np.random.randint(20, size=array_size)
        else: P[j,:] = np.zeros(array_size)
    print(P)

    try:
        now = time.time()
        print('Solution 1 is:')
        sol1 = solution(np.ndarray.tolist(P))
        print(sol1)
        print(f'passed = {time.time()-now}')
        now = time.time()
        print('Solution 2 is:')
        sol2 = solution2(np.ndarray.tolist(P))
        print(sol2)
        print(f'passed = {time.time()-now}')
    except:pass    
    assert sol1==sol2