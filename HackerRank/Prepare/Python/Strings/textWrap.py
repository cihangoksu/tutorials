# %% text wrap
import textwrap
from turtle import width

def wrap(string, max_width):
    wrapped = textwrap.wrap(string, width)
    for word in wrapped: print(word)


if __name__ == '__main__':
    string, width = 'ABCDCDC', 4
    
    wrap(string, width)
