# %% default dict
from collections import defaultdict
def print_output(A_list, B_list):
    group_A = defaultdict(list)

    for i, item_i in enumerate(A_list):
        group_A[item_i].append(i+1)
    
    for i, item_i in enumerate(B_list):
        if item_i in group_A.keys():
            print(' '.join(map(str,group_A[item_i])))
    

if __name__ == '__main__':

    m, n = 5,2
    A_list = 'a a b a b'.split()
    B_list = 'a b'.split()

    print_output(A_list, B_list)





    pass
    
    


    
