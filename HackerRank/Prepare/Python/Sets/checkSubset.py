# %% if A is a subset of B
if __name__ == '__main__':
    A = set('1 2 3 5 6'.split())
    B = set('9 8 5 6 3 2 1 4 7'.split())
    if A == A.intersection(B): print(True)
    else: print(False)
    


    
