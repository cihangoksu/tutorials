# %% Sets intro

def average(array):
    # your code goes here
    set_arr = set(array)
    return sum(set_arr)/len(set_arr)


if __name__ == '__main__':
    n = 10
    arr = list(map(int, '161 182 161 154 176 170 167 171 170 174'.split()))
    result = average(arr)
    print(result)

    