# %% List solution
import time 
from copy import deepcopy
from itertools import permutations

#----Bellman Ford algo----
def get_shortest_path(start_node, times):
    num_nodes = len(times)       
    my_inf = 10**100
    node_list = [my_inf]*(start_node)+[0]+[my_inf]*(num_nodes-start_node-1) 
    target_list = list(range(num_nodes))
    target_list.remove(start_node)
    for i in range(num_nodes-1):
        # iteration num i
        for j in range(num_nodes):
            for k in target_list:
                node_list[k] = min(node_list[k], node_list[j] + times[j][k])

    # One more time against negative cycles    
    node_list_legacy = deepcopy(node_list)

    for j in range(num_nodes):
        for k in target_list:
            node_list[k] = min(node_list[k], node_list[j] + times[j][k])
    
    if node_list_legacy!=node_list: neg_cycle=True
    else: neg_cycle=False
    return node_list, neg_cycle

def solution(times, times_limit):
    shortest_times = []
    for i in range(len(times)):
        start_node = i
        node_list, neg_cyc = get_shortest_path(start_node, times)
        if neg_cyc: return list(range(0,len(times)-2))
        shortest_times.append(node_list)

    bunny_indeces = list(range(1,len(times)-1))
    available_paths = []
    for i in range(len(bunny_indeces),0,-1):
        bunny_perm = list(permutations(bunny_indeces,i))
        for ind_list in bunny_perm:
            current_node = 0
            time_needed = 0
            for j in ind_list:
                time_needed += shortest_times[current_node][j]
                current_node = j
            time_needed += shortest_times[current_node][-1]
            if time_needed<=times_limit: available_paths.append(ind_list)
        if available_paths: break
    
    available_paths_sorted = sorted(available_paths, key=lambda pair: pair[0], reverse=False)
    if available_paths_sorted: return list(map(lambda x:x-1, sorted(available_paths_sorted[0])))
    else: return []





# input_list, time_zero = [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1
# input_list, time_zero = [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3
#input_list, time_zero = [[0, 10, 10, 1, 10],[10, 0, 10, 10, 1],[10, 1, 0, 10, 10],[10, 10, 1, 0, 10],[1, 10, 10, 10, 0]],6


input_list, time_zero = [[0, 2, 2, 2, -1],[9, 0, 2, 2, 0],[9, 3, 0, 2, 0],[9, 3, 2, 0, 0],[-1, 3, 2, 2, 0]],-500

now = time.time()
output = solution(input_list, time_zero)
print(output)
print(f'Elapsed time {(time.time()-now)*1000}')







if __name__ == '__main__':
    case1 = [[0, 1, 1, 1, 1],
             [1, 0, 1, 1, 1],
             [1, 1, 0, 1, 1],
             [1, 1, 1, 0, 1],
             [1, 1, 1, 1, 0]]
    print("\n\nCase 1: Provided test case 1.\nTime limit: 3")
    for row in case1:
        print('', row)
    print("\n  Expected: [0, 1]\nCalculated:", str(solution(case1, 3)))

    print("\n\nCase 2: Provided test case 2.\nTime limit: 1")
    case2 = [[0, 2, 2, 2, -1],
             [9, 0, 2, 2, -1],
             [9, 3, 0, 2, -1],
             [9, 3, 2, 0, -1],
             [9, 3, 2, 2, 0]]
    for row in case2:
        print('', row)
    print("\n  Expected: [1, 2]\nCalculated:", str(solution(case2, 1)))







    print("\n\nCase 3: Infinite negative cycle.\nTime limit: -500")
    case3 = [[0, 2, 2, 2, -1],
             [9, 0, 2, 2, 0],
             [9, 3, 0, 2, 0],
             [9, 3, 2, 0, 0],
             [-1, 3, 2, 2, 0]]
    for row in case3:
        print('', row)
    print("\n  Expected: [0, 1, 2]\nCalculated:", str(solution(case3, -500)))

    print("\n\nCase 4: Max bunnies. None rescuable.\nTime limit: 1")
    case4 = [[1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1]]
    for row in case4:
        print('', row)
    print("\n  Expected: []\nCalculated:", str(solution(case4, 1)))

    print("\n\nCase 5: One bunny.\nTime limit: 2")
    case5 = [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]]
    for row in case5:
        print('', row)
    print("\n  Expected: [0]\nCalculated:", str(solution(case5, 2)))

    print("\n\nCase 6: Multiple revisits.\nTime limit: 10")
    case6 = [[0, 5, 11, 11, 1],
             [10, 0, 1, 5, 1],
             [10, 1, 0, 4, 0],
             [10, 1, 5, 0, 1],
             [10, 10, 10, 10, 0]]
    for row in case6:
        print('', row)
    print("\n  Expected: [0, 1]\nCalculated:", str(solution(case6, 10)))

    print("\n\nCase 7: Multiple Revisits 2.\nTime limit: 5")
    case7 = [[0, 10, 10, 10, 1],
             [0, 0, 10, 10, 10],
             [0, 10, 0, 10, 10],
             [0, 10, 10, 0, 10],
             [1, 1, 1, 1, 0]]
    for row in case7:
        print('', row)
    print("\n  Expected: [0, 1]\nCalculated:", str(solution(case7, 5)))

    print("\n\nCase 8: Time travel.\nTime limit: 1")
    case8 = [[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]
    for row in case8:
        print('', row)
    print("\n  Expected: [0, 1, 2]\nCalculated:", str(solution(case8, 1)))

    print("\n\nCase 9: No bunnies.\nTime limit: 1")
    case9 = [[2, 2],
             [2, 2]]
    for row in case9:
        print('', row)
    print("\n  Expected: []\nCalculated:", str(solution(case9, 1)))

    print("\n\nCase 10: Backwards bunny path.\nTime limit: 6")
    case10 = [[0, 10, 10, 1, 10],
              [10, 0, 10, 10, 1],
              [10, 1, 0, 10, 10],
              [10, 10, 1, 0, 10],
              [1, 10, 10, 10, 0]]
    for row in case10:
        print('', row)
    print("\n  Expected: [0, 1, 2]\nCalculated:", str(solution(case10, 6)))



