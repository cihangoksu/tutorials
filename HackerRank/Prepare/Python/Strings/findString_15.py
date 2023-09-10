# %% find a string
from re import sub

#.strip is used to get rid of leading and trailing whitespaces or given characters

def count_substring(string, sub_string):
    count = 0
    for idx, itx in enumerate(string):
        item = string[idx:idx+len(sub_string)]
        if item == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = 'ABCDCDC'
    sub_string = 'CDC'
    
    count = count_substring(string, sub_string)
    print(count)