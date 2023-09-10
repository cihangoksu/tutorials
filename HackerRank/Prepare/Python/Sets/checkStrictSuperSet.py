# %% if A is a subset of B
if __name__ == '__main__':
    A = set('1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78'.split())

    B1 = set('1 2 3 4 5'.split())
    B2 = set('100 11 12'.split())

    if B1 == B1.intersection(A) and len(A)>len(B1):
        if B2 == B2.intersection(A) and len(A)>len(B2): print(True)
        else: print(False)    
    else: print(False)
    


    
