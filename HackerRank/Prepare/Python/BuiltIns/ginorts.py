from curses.ascii import isdigit


input_str = 'Sorting1234'
input_list = list(input_str)
def check_odd(x): 
    if x.isdigit():
        if int(x)%2==1: return True
    return False
def check_even(x): 
    if x.isdigit():
        if int(x)%2==0: return True
    return False

odd_digit_list = sorted(filter(check_odd, input_list))
even_digit_list = sorted(filter(check_even, input_list))
lower_list = sorted(filter(lambda x:x.islower(), input_list))
upper_list = sorted(filter(lambda x:x.isupper(), input_list))
output_list = lower_list+upper_list+odd_digit_list+even_digit_list

print(''.join(output_list))







