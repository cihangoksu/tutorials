# %% regex
import re
vowels = 'AEIOUaeiou'
consonents = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'

regex_pattern = r"[AEIOUaeiou]"	# Do not delete 'r'.

char_list = re.findall(regex_pattern,'http://www.haaackerrank.com/')
print(char_list)


# printIt = ''
# for idc, myChar in enumerate(char_list):
#     if myChar in vowels:
#         first_id = idc

#     printIt += myChar 

