# %% Merge the tools

def merge_the_tools(string, k):
    str_list = []
    for idx in range(len(string)//k):
        mylist = string[idx*k:idx*k+k]
        sorted_list = list(dict.fromkeys(mylist))
        print(''.join(sorted_list))
    return




if __name__ == '__main__':
    string, k = 'AABCAAADA', 3
    merge_the_tools(string,k)