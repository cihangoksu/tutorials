import threading

event = threading.Event()

def myfunction():
    print('Waiting for trigger...\n')
    event.wait()
    print('Performing action xyz now...')

t1 = threading.Thread(target=myfunction)
t1.start()

x = input('Shall we trigger the event? y/n?\n')
if x=='y':
    event.set()

    