# %% List solution
'''
def solution(M,F): # Mach bombs and Facula bombs
    mf_list = [int(M), int(F)]
    if mf_list == [1,1]: return 0
    n = 0
    while True:
        sorted_list = sorted(mf_list)
        if 0 in mf_list: return 'impossible'
        elif mf_list == [1,2]: return str(n+1)
        else: pass
        mf_list = [sorted_list[0],sorted_list[1]-sorted_list[0]]
        n += 1 
'''
# %% generators solution
def solution(M,F): # Mach bombs and Facula bombs
    speedUp = False
    if len(M) > 2 or len(F) > 2: speedUp = True
    if M == '0' or F == '0': return 'impossible'
    elif M == '1' and F == '1': return '0'
    elif (M == '1' and F == '2') or (M == '2' and F == '1'): return '1'
    sorted_list = sorted([int(M), int(F)])
    
    if sorted_list[0]==1: return str(sorted_list[1]-1)
    elif sorted_list[1]%sorted_list[0] == 0: return 'impossible'
    else:pass
    
    n = 0
    while True:
        if 0 in sorted_list: return 'impossible'
        elif sorted_list == [1,1]: return str(n)
        elif sorted_list[0] == 1: return str(sorted_list[1]-1+n)
        else: pass
        
        sorted_list[0] = min(sorted_list[0],sorted_list[1]-sorted_list[0])
        try: k = (sorted_list[1]//sorted_list[0]-1)
        except ZeroDivisionError: return 'impossible'
        sorted_list = sorted([sorted_list[0],sorted_list[1] - k*sorted_list[0]])
        n += k 
        




M = '3'
F = '7'
import time 
now = time.time()
print(solution(M,F))
print(f'Elapsed time {(time.time()-now)*1000}')
print('completed')











