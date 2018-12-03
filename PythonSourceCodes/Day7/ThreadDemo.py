# Multithreading in Python

import threading
import time

def loop1To10():
    for i in range(1,11):
        time.sleep(2)  # Sleeps every 1 sec
        print(i)

def loopAToT():
    for j in range(65,86):
        time.sleep(1)
        print(chr(j))        

threading.Thread(target=loop1To10).start()
threading.Thread(target=loopAToT).start()

