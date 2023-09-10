def are_they_equal(array_a, array_b):
  # Write your code here
  
  while len(array_a)>0:
    for i in range(len(array_a)):
      if array_a[i]==array_b[i]:
        array_a.remove(array_a[i])
        array_b.remove(array_b[i])
        break
      elif (array_a[i]!=array_b[i]) and len(array_a)==1:
        return False
      else:
        for k in range(2,len(array_a)+1): #2,3
          equal_subarray_found = False
          if array_b[0:k][::-1] == array_a[0:k]:
            equal_subarray_found = True
            try:
                del array_a[0:k]
                del array_b[0:k]
            except:
              import pdb; pdb.set_trace()
            break

        if equal_subarray_found: break
        else: return False
  return True 

A = [1, 2, 3, 4]
B = [1, 2, 3, 5]

output = are_they_equal(A,B)
print(output)