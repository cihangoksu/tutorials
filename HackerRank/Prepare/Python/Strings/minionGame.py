# %% minion game
import time
# Complete the solve function below.
def minion_game(string):
    myStr = string.lower()
    
    now = time.time()

    stuart_score, kevin_score = 0, 0

    for idx in range(len(myStr)):
        if myStr[idx] in 'aeiou':
            kevin_score += len(myStr) - idx
        else:
            stuart_score += len(myStr) - idx

    passed = time.time()-now
    print(passed*1000)

    if stuart_score==kevin_score:
        print(f'Draw')
    elif max(stuart_score, kevin_score) == stuart_score:
        print(f'Stuart {stuart_score}')
    elif max(stuart_score, kevin_score) == kevin_score:
        print(f'Kevin {kevin_score}')
    else:
        pass
    
    return


if __name__ == '__main__':
    s = 'BANAna'
    minion_game(s)