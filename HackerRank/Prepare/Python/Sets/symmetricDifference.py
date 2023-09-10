# %% Symmetric difference
def symmetric_difference(a,b):
    diff = None
    a_set = set(a.split())
    b_set = set(b.split())

    ''' same thing
    a_diff_b = a_set.difference(b_set)
    b_diff_a = b_set.difference(a_set)
    diff_set = a_diff_b.union(b_diff_a)
    '''
    diff_set = a_set.symmetric_difference(b_set)

    diff = list(diff_set)

    sorted_diff = list(map(str,sorted(map(int, diff))))

    for itx in sorted_diff: print(itx)

    return sorted_diff



if __name__ == '__main__':
    M = 3
    a = '9 10 11'
    N = 3
    b = '10 11 13'
    symmetric_difference(a,b)
