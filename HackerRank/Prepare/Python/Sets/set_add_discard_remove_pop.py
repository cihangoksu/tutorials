n = 9
s = set(map(int, '1 2 3 4 5 6 7 8 9'.split())) 
cmd_line = 'remove 3 5'
cmd, *val = cmd_line.split()
val_str = " ".join(val)
if val: eval(f's.{cmd}({val_str})')
else: val: eval(f's.{cmd}()')
print(sum(s))