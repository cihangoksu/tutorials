from typing import List
# Write any import statements here
import numpy as np
def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  # Write your code here
  occupied_seat_length = K+1
  sorted_S = sorted(S)
  total_diners = 0
  for idx,x in enumerate(sorted_S):
    if idx != 0: 
      pre_diners = int(np.ceil((x-K-sorted_S[idx-1])/occupied_seat_length-1))
    else: 
      pre_diners = int(np.ceil(x/occupied_seat_length-1))
    total_diners+=pre_diners
  
  pre_diners = int(np.ceil((N+1-sorted_S[-1])/occupied_seat_length-1))
  total_diners+=pre_diners

  return total_diners

print(getMaxAdditionalDinersCount(N = 10, K = 1, M = 3, S = [3, 7])) #2
print(getMaxAdditionalDinersCount(N = 10, K = 1, M = 2, S = [2, 6])) #3
print(getMaxAdditionalDinersCount(N = 15, K = 2, M = 2, S = [11, 6, 14])) #1
