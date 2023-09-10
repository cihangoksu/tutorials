# %%
n = 50
if n%2 == 1:
    print('Weird')
elif (n%2 == 0) and (2<=n<=5):
    print('Not Weird')
elif (n%2 == 0) and (6<=n<=20):
    print('Weird')
elif (n%2 == 0) and (20<=n<=100):
    print('Not Weird')
else:
    import pdb; pdb.set_trace()
    print('Not accepted number')


