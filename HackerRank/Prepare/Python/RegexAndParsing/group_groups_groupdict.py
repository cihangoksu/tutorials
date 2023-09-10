# %% Itertools solution
'''
input_str = '..12345678910111213141516171820212223'
from itertools import groupby
for key,group in groupby(input_str):
    #print(key)
    #print(list(group))
    if len(list(group))>1 and key.isalnum(): 
        repeating_char = key
        break

'''

# %% regex solution
import re
input_str = '..12345678910111213141516171820212223'
matcher = re.compile(r'(.)\1*')
bLetterExist = False
for match in matcher.finditer(input_str): 
    m = match.group()
    if len(m)>1 and m[0].isalnum(): 
        bLetterExist = True
        break
if bLetterExist: print(m[0])
else: print('-1')