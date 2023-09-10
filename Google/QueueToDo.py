# ref: https://www.geeksforgeeks.org/find-xor-of-numbers-from-the-range-l-r/
from operator import xor
def findXOR(n):
    mod = n % 4
    if (mod == 0): return n
    elif (mod == 1): return 1
    elif (mod == 2): return n + 1
    elif (mod == 3): return 0
 
def findXORFun(l, r):
    return (xor(findXOR(l - 1) , findXOR(r)))
 
def solution(start, length):
    if length==1: return start
    workers = length
    checksum_list = []
    while workers>0:
        s,l = start, start + workers-1
        checksum_list.append(findXORFun(s, l))
        start += length
        workers-=1

    checksum = checksum_list[0]^checksum_list[1]
    for item in checksum_list[2:]: 
        checksum = checksum^item
     
    return checksum

print(solution(0,1))
