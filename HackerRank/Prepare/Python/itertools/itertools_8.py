from itertools import product, permutations, combinations, combinations_with_replacement

# %% Iter tools product
'''
def convert_to_list(input_string):
    mylist = list(map(int,input_string.split(' ')))
    return mylist

if __name__ == '__main__':
    list_A = convert_to_list(str(input()))
    list_B = convert_to_list(str(input()))
    prod_AB = list(product(list_A,list_B))
    std_out = ' '.join(str(x) for x in prod_AB)
    print(sorted(prod_AB))
    print(std_out)

    
'''

# %% Iter tools permutations
'''
if __name__ == '__main__':
    string_input = str(input()) # HACK 2
    name, perm_num = string_input.split(' ')
    perm_out = permutations(name.upper(),int(perm_num))
    for std_out in sorted(perm_out):
        print(''.join(std_out))
'''



# %% Iter tools combinations
'''
if __name__ == '__main__':
    string_input = str(input()) # HACK 2
    name, comb_num = string_input.split(' ')
    for idx in range(int(comb_num)):
        comb_out = list(combinations(name.upper(),int(idx + 1)))
        comb_out_sorted = []
        for std_out in comb_out:
            comb_out_sorted.append(sorted(std_out))

        for std_out in sorted(comb_out_sorted):
            print(''.join(std_out))


'''

# %% Combinations with replacement
if __name__ == '__main__':
    string_input = str(input()) # HACK 2
    name, comb_num = string_input.split(' ')

    comb_out = list(combinations_with_replacement(name.upper(),int(comb_num)))
    comb_out_sorted = []
    for std_out in comb_out:
        comb_out_sorted.append(sorted(std_out))

    for std_out in sorted(comb_out_sorted):
        print(''.join(std_out))


