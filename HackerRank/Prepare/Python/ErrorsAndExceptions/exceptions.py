


def divide_it (a,b):
    try: 
        c = int(a)//int(b)
        print(c)
    except ZeroDivisionError as e: print(f'Error Code:{e}')
    except ValueError as e: print(f'Error Code: {e}')
        
    
    

if __name__ == '__main__':
    a,b = '1','0'
    a,b = '2','$'
    # a,b = '3','1'

    divide_it(a,b)