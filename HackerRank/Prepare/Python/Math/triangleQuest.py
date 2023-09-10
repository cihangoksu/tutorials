# %% triangle quest

N = 5
for i in range(1, N):
    mult = list(map(lambda x:10**x, list(range(i))))
    x = sum(map(lambda x:x*i, mult))
    print(x)

    
