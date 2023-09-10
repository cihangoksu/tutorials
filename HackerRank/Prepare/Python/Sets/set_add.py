# %% set add
from collections import Counter
def get_stamps(country_list):
    dict_list = Counter(country_list)
    return len(dict_list)



if __name__ == '__main__':
    line1 = '7'
    country_list = ['UK','China','USA','France','New Zealand','UK','France']
    print(get_stamps(country_list))
