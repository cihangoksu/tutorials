# %% set add
""" 
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66

 """

if __name__ == '__main__':
    N = 16
    A = set('1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52'.split())
    M = 4
    for i in range(2*M):
        line = input()
        if i % 2 == 0: 
            cmd, _ = line.split()
        else:
            other_set = set(line.split())
            eval(f'A.{cmd}({other_set})')

    print(A)
    
