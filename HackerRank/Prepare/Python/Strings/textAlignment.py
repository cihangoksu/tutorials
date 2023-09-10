# %% textalignment


def draw_logo(width):
    for idx in range(0,2*width,2):
        myStr = 'H'*(idx+1)
        print(myStr.center(2*width-1))
        # print(myStr.ljust(2*width-1))
        # print(myStr.rjust(2*width-1))


    h_full = 'H'*width
    line1 = ' '*((width-1)//2)
    line1 += 'H'*width
    line1 += h_full.rjust(width*4)
    for idx in range(width+1):
        print(line1)

    line2 = ' '*((width-1)//2)
    line2 += 'H'*(width*5)
    for idx in range((width+1)//2):
        print(line2)

    for idx in range(width+1):
        print(line1)
    
    for idx in range(2*width,0,-2):
        myStr = 'H'*(idx-1)
        myStr = ' '*width*4 + myStr.center(2*width-1)
        print(myStr)
        
    

if __name__ == '__main__':
    width = 5
    draw_logo(width)
