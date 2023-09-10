import time
import threading

def func1():
    secs = 60
    for idx in range(60):
        print(f'{secs}')
        time.sleep(1)
        secs -= 1

def func2():
    hsecs = 120
    for idx in range(120):
        print(f'{hsecs}')
        time.sleep(0.5)
        hsecs -= 1


t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)
t1.start()
t2.start()

# t1.join()
# print('Thread 1 is completed')