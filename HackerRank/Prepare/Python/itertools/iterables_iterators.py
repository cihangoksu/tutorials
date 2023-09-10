from itertools import combinations
input_list = 'a a c d'.split()
k = 2

comb_list = list(combinations(input_list,k))
bool_list = list(map(lambda x:('a' in x)    ,comb_list))
prob = len(list(filter(lambda x:x, bool_list)))/len(bool_list)

print(prob)

