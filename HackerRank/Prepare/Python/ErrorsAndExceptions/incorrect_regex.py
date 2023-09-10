import re
def try_reg(pattern):
    try: 
        re.compile(pattern)
        return True
    except: 
        return False
    
if __name__ == '__main__':
    pattern = r'.*/+'
    print(try_reg(pattern))
