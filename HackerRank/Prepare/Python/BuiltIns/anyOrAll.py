input = '12 9 61 5 14'
input_list_int = list(map(int,input.split()))
bool_list = list(map(lambda x:x>0, input_list_int))
cond1 = all(bool_list)

input_list_str = input.split()
bool_list_2 = list(map(lambda x:x==x[::-1],input_list_str))
cond2 = any(bool_list_2)

print(cond1 and cond2)

