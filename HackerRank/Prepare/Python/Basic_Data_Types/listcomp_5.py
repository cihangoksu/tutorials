# %%
x = 1
y = 1
z = 2
n = 3
from itertools import product
myPermute = product(list(range(x+1)),list(range(y+1)),list(range(z+1)) )
out_list = []
for itemx in myPermute:
    print(itemx)
    if sum(itemx)!= n:
        out_list.append(list(itemx))
print(out_list)
