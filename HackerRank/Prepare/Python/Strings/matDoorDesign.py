# %% string formatting
def print_formatted(number):
    line_dec = list(range(1,number+1,1))
    line_oct, line_hex, line_bin = [], [], []
    for idx, itx in enumerate(line_dec):
        conv_oct, conv_hex, conv_bin = format(itx,'o'), format(itx,'X'), format(itx,'b')
        line_oct.append(conv_oct)
        line_hex.append(conv_hex)
        line_bin.append(conv_bin)
    print(line_oct)
    print(line_hex)
    print(line_bin)

    max_length = len(line_bin[-1])+1
    line_comb = []
    for idx, itx in enumerate(line_dec):
        line = f'{line_dec[idx]}'.rjust(max_length-1) + f'{line_oct[idx]}'.rjust(max_length) + f'{line_hex[idx]}'.rjust(max_length) + f'{line_bin[idx]}'.rjust(max_length)  
        print(line)



if __name__ == '__main__':
    print_formatted(17)