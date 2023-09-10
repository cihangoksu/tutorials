from itertools import product

def get_maximized_S(input_list, M):
    K = len(input_list)
    f_x_list = []
    for mylist in input_list:
        f_x_list.append(sorted(list(map(lambda x: x**2, mylist))))

    prod_list = product(*f_x_list)

    max_sum = 0
    for arr in prod_list:
        max_sum = max(max_sum,sum(arr)%M)

    return max_sum

#%% Combinations with replacement
if __name__ == '__main__':
    K = 3
    M = 1000
    array_list = []
    array_list.append(list(set(map(int,'2 5 4'.split()))))
    array_list.append(list(set(map(int,'3 7 8 9'.split()))))
    array_list.append(list(set(map(int,'5 5 7 8 9 10'.split()))))

    print(get_maximized_S(array_list, M))






