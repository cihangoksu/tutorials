# %% ordered dictionary

from collections import deque


def pile_up(block_array):
    border_block = [block_array[0], block_array[-1]]
    max_size_prev = max(border_block)

    while len(block_array)>0:
        try: 
            border_block = [block_array[0], block_array[-1]]
            max_size = max(border_block)
            if max_size_prev<max_size: return False
        except IndexError: break
        if border_block.index(max_size)==0: block_array.popleft()
        else: block_array.pop()
        max_size_prev = max_size
    return True
""" 
        if len(block_array)<=1: return True
        else: return False

 """
if __name__ == '__main__':
    block_array = deque('4 3 2 1 3 4'.split())
    # block_array = list(map(int,'1 3 2'.split()))
    print(pile_up(block_array))
    
