# %% find a string
'''
In the first line, print True if has any alphanumeric characters. Otherwise, print False.
In the second line, print True if has any alphabetical characters. Otherwise, print False.
In the third line, print True if has any digits. Otherwise, print False.
In the fourth line, print True if has any lowercase characters. Otherwise, print False.
In the fifth line, print True if has any uppercase characters. Otherwise, print False. 
'''


def validate(string):
    line_out =[False]*5
    for letter in string:
        if letter.isalnum():
            line_out[0]=True
        if letter.isalpha():
            line_out[1]=True
        if letter.isdigit():
            line_out[2]=True
        if letter.islower():
            line_out[3]=True
        if letter.isupper():
            line_out[4]=True
    for line in line_out:
        print(line)
    
    
    

if __name__ == '__main__':
    string = 'ABCDCDC'
    
    validate(string)
