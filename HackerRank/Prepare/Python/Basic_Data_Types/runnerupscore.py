n = 5
arr = map(int, [2,3,6,6,5])
mylist = list(arr)
max_elem = max(mylist)
while max_elem in mylist:
    mylist.remove(max_elem)
# rUp = getRunnerUp(n, arr)
print(max(mylist))