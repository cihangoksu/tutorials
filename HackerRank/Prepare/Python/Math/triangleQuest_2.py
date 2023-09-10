# %% triangle quest 2
""" 
1                 1*1
121               11*11
12321             111*111
"""
N = 5
for i in range(1,int(N)+1):
    print(sum(map(lambda x: 10**x, range(i)))**2)
    


    
