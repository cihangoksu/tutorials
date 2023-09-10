# %% Compress a string
string_input = str(input())
inp_list = list(string_input)
count = 0
out_list = []
for idx,itx in enumerate(inp_list[:-1]):
    if itx == inp_list[idx+1]:
        count += 1
    else:
        tpl = (count+1,int(itx))
        out_list.append(str(tpl))
        count = 0

tpl = (count+1,int(inp_list[-1]))
out_list.append(str(tpl))
print(' '.join(out_list))

