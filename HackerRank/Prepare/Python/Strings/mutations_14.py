# %% split and join strings
def mutate_string(string, position, character):
    splitted = list(string)
    splitted[position] = character
    joinned = ''.join(splitted)
    return joinned

if __name__ == '__main__':
    s = 'abracadabra'
    i, c = '5', 'k'
    s_new = mutate_string(s, int(i), c)
    print(s_new)