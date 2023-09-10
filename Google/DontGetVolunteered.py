def map_i_xy(i):
    x,y = i % 8, i//8
    return [x,y]

def solution(isrc, idest):
    N = 8
    src, dest = map_i_xy(isrc),map_i_xy(idest)
    distance = list(map(abs, sorted([dest[0]-src[0], dest[1]-src[1]])))
    nMove = 0

    while distance[0]>2 or distance[1]>2:
        distance = sorted(distance)
        distance[0] -= 1
        distance[1] -= 2
        distance = list(map(abs,distance))
        nMove += 1
    if distance == [1,1] or distance == [0,2]:
        nMove += 2
    if distance == [0,1]:
        nMove += 3
    if distance == [1,2]:
        nMove += 1
    if distance == [2,2]:
        nMove += 4

    return nMove

import time
now = time.time()
print(solution(7,53))
print((time.time()-now)*1000)

for i in range(2):
    for j in range(2):
        if i != j:
            print(solution(i,j))