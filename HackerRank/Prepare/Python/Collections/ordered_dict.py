# %% ordered dictionary
from collections import OrderedDict

'''
4
bcdef
abcdefg
bcde
bcdef
'''

if __name__ == '__main__':
    N = 4
    word_dict = OrderedDict()

    for i in range(N):
        word = input()

        try: word_dict[word] += 1
        except KeyError: word_dict[word] = 1

    print(len(word_dict))
    print(' '.join(map(str,word_dict.values())))
    

