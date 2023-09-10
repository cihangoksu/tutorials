# %% ordered dictionary
from collections import deque

'''
6
append 1
append 2
append 3
appendleft 4
pop
popleft
'''
def apply_command(command, d):
    cmd, *val = command.split()
    
    if val: eval(f'd.{cmd}({val[0]})')
    else: eval(f'd.{cmd}()')
    return d


if __name__ == '__main__':
    N = 6
    d = deque()
    for i in range(N):
        command = input()
        d = apply_command(command, d)

    print(' '.join(list(map(str,d))))


    
