# %% set add
from cmath import phase
if __name__ == '__main__':
    x,y = 0,0
    input = '-1-5j'
    flag_minus = False
    if input[0] == '-':
        input = input[1:]
        flag_minus = True
    if 'j' in input:
        if '+' in input: x,y = map(int,input[:-1].split('+'))
        elif '-' in input: 
            x,y = map(int,input[:-1].split('-'))
            y = -y
        else: y = int(input[:-1])
    else: 
        x = int(input)
    if flag_minus:
        x = -x

    print('{:.3f}'.format(abs(complex(x,y))))
    print('{:.3f}'.format(phase(complex(x,y))))
    pass

    


    
