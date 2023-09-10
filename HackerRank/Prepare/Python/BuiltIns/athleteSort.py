N,M = 5,3
input_list = []
input_list.append(list(map(int,'10 2 5'.split())))
input_list.append(list(map(int,'7 1 0'.split())))
input_list.append(list(map(int,'9 9 9'.split())))
input_list.append(list(map(int,'1 23 12'.split())))
input_list.append(list(map(int,'6 5 9'.split())))
K =1

sorted_list = sorted(input_list, key = lambda x:x[K])

for inner_list in sorted_list: 
    mylist = list(map(str,inner_list))
    print(' '.join(mylist))


