# Enter your code here. Read input from STDIN. Print output to STDOUT
'1 4'
'x**3 + x**2 + x + 1'

x,y = list(map(int,input().split()))
input_string = input()
out = eval(input_string)
print(out==y)