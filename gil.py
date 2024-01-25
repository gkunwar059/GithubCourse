import threading
import time

def print_numbers():
    for i in range(4):
        print(i)
        # time.sleep(1)

thread=threading.Thread(target=print_numbers)
thread1=threading.Thread(target=print_numbers)
thread.start()
thread1.start()