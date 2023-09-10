# %% set unions
if __name__ == '__main__':
    M = '9'
    English = '1 2 3 4 5 6 7 8 9'
    N = '9'
    French = '10 1 2 3 11 21 55 6 8'

    set_eng = set(English.split())
    set_fr = set(French.split())
    print(len(set_eng.union(set_fr)))

    print(len(set_eng.intersection(set_fr)))

    print(len(set_eng.difference(set_fr)))