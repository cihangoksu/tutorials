'''
Consider a list (list = []). You can perform the following commands:

    insert i e: Insert integer 

at position
.
print: Print the list.
remove e: Delete the first occurrence of integer
.
append e: Insert integer

    at the end of the list.
    sort: Sort the list.
    pop: Pop the last element from the list.
    reverse: Reverse the list.

Initialize your list and read in the value of
followed by lines of commands where each command will be of the types listed above. Iterate through each command in order and perform the corresponding operation on your list. 

'''
input_list = []
def apply_command(command):
    global input_list

    cmd = command.split(' ')
    out_list = input_list.copy()
    if cmd[0] == 'insert':
        input_list.insert(int(cmd[-2]),int(cmd[-1]))
    elif cmd[0] == 'print':
        print(input_list)
    elif cmd[0] == 'remove':
        input_list.remove(int(cmd[-1]))
    elif cmd[0] == 'append':        
        input_list.append(int(cmd[-1]))
    elif cmd[0] == 'sort':
        input_list.sort()        
    elif cmd[0] == 'pop':
        input_list.pop(-1)
    elif cmd[0] == 'reverse':
        input_list.reverse()        
    else:
        print(f'wrong command: {command}')
    
    return input_list


while True:
    cmd = str(input())
    output_list = apply_command(cmd)
    print(output_list)

    






