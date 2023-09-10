# %% default dict
from collections import namedtuple
    
""" 
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6 
"""
if __name__ == '__main__':
    N = 5
    columns = 'ID         MARKS      NAME       CLASS'.split()
    Student = namedtuple('student', ','.join(columns))

    avg = 0
    for i in range(N):
        input_values = input().split()
        student = Student(*input_values)
        avg+=int(student.MARKS)/N
    

    print('{:.2f}'.format(avg))

    
    


    
