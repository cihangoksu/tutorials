#### Standard queue
'''
import queue

q = queue.Queue()

# 1,2,3,4,5
# 1
# 2,3,4,5

numbers = range(10,80,10)

for number in numbers:
    q.put(number)

print(q.get())
print(q.get())


'''


#### Lifo queue
'''
import queue
q = queue.LifoQueue()

# 1,2,3,4,5
# 1
# 2,3,4,5

numbers = range(10,80,10)

for number in numbers:
    q.put(number)

print(q.get())
print(q.get())

'''


#### Priority queue

import queue
q = queue.PriorityQueue()



q.put((2, 'hello world'))
q.put((11, 99))
q.put((5, 7.5))
q.put((1, True))

while not q.empty():
    print(q.get())


