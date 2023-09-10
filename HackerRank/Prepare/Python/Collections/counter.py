# %% set add
from collections import Counter
if __name__ == '__main__':

    X = '10'
    shoe_dict = Counter('2 3 4 5 6 8 7 6 5 18'.split())
    N = '6'
    '''
    '6 55'
    '6 45'
    '6 55'
    '4 40'
    '18 60'
    '10 50'
    '''
    earnings = 0
    for i in range(int(N)):
        shoe_size, price = input().split()
        if shoe_dict[shoe_size] >0: 
            earnings += int(price)
            shoe_dict[shoe_size] -= 1
        
    print(earnings)
    pass
    
    


    
