# %% set add
from collections import Counter
if __name__ == '__main__':
    K = 5
    rooms = '1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2'.split()
    rooms_dict = Counter(rooms)
    list(rooms_dict.keys())[list(rooms_dict.values()).index(1)]    
    pass
    
    


    
