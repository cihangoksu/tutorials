# %% rangoli
from audioop import reverse
import string
def print_rangoli(size):
    length = (size-1)*4+1
    alphabet_string = string.ascii_lowercase
    alpha = list(alphabet_string[:size])
    alpha_r = list(alpha[::-1])
    
    for idx in range(1,size+1):
        line = '-'.join(alpha_r[:idx] + alpha_r[:idx-1][::-1])
        print(line.center(length, '-'))

    for idx in range(size-1,0,-1):
        line = '-'.join(alpha_r[:idx] + alpha_r[:idx-1][::-1])
        print(line.center(length, '-'))




if __name__ == '__main__':
    print_rangoli(3)