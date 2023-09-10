# %% Itertools solution
'''
4
4.0O0
-1.00
+4.54
SomeRandomStuff
'''
# %% detect floating
def test_floating(input_str):
    bIsFloating = True
    allowed_string = '+-.'+''.join(list(map(str,list(range(10)))))
    # Test case 1:
    for myChar in input_str:
        if not(myChar in allowed_string): return False 
    if '+' in input_str: 
        if not(input_str[0] == '+'): return False
    if '-' in input_str: 
        if not(input_str[0] == '-'): return False  
    if input_str.count('+')>1 or input_str.count('-')>1 or input_str.count('.')>1: return False 
    if input_str.split('.')[-1] == '': return False
    if input_str.count('.') != 1: 
        try: 
            x = int(input_str)
            if x == 0: return False
        except: return False
    try: float(input_str)
    except: return False

    return bIsFloating


print(test_floating('5'))
print(test_floating('1.414'))
print(test_floating('+.5486468'))
print(test_floating('0.5.0'))
print(test_floating('1+1.0'))
print(test_floating('0'))

# import re
# input_str = '..12345678910111213141516171820212223'
# matcher = re.compile(r'(.)\1*')
# bLetterExist = False
# for match in matcher.finditer(input_str): 
#     m = match.group()
#     if len(m)>1 and m[0].isalnum(): 
#         bLetterExist = True
#         break
# if bLetterExist: print(m[0])
# else: print('-1')