import numpy as np
import sympy as sy

# %%
def solution(matrix):
    num_terminal = 0
    P = sy.Matrix(matrix)
    for i, row in enumerate(matrix):
        if sum(map(abs, row)) == 0:
            num_terminal += 1
            arr = sy.zeros(1,len(row))
            arr[i] = 1
            P[i,:] = arr
        else:
            for j, elem in enumerate(row):
                if elem == 0: P[i,j] = 0 
                else: P[i,j] = sy.Rational(elem/sum(row))
            
        
    num_transient = len(matrix)-num_terminal
    
    Q = P[0:num_transient,0:num_transient]
    R = P[0:num_transient, num_transient:]

    F2Invert = sy.eye(num_transient) - Q
    F = F2Invert.inv()
    M = F*R

    from sympy import nsimplify
    num_array, denom_array = np.zeros(num_terminal), np.zeros(num_terminal)
    for i in range(num_terminal):
        simplified = nsimplify(M[0,i])
        numerotor, denominator = simplified.as_numer_denom()
        num_array[i], denom_array[i] = numerotor, denominator
    
    denominator = np.lcm.reduce(list(map(int,np.ndarray.tolist(denom_array))))


    denom_weights = denominator/denom_array
    num_array = num_array*denom_weights
    num_list = np.ndarray.tolist(num_array)
    result = list(map(int,num_list + [denominator]))

    return result



P = [[0, 1, 0, 0, 0, 1], 
    [4, 0, 0, 3, 2, 0], 
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0]]

""" P = [[0, 2, 1, 0, 0], 
    [0, 0, 0, 3, 4], 
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0]]
 """


print(solution(P))