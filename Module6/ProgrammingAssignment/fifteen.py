# Python V 3.9.0

import threading
import random
import time

def processOne(start):
    rand = random.random()
    time.sleep(rand)
    end = time.time()
    current = end - start
    print(str(current) + " process one")

def processTwo(start):
    rand = random.random()
    time.sleep(rand)
    end = time.time()
    current = end - start
    print(str(current) + " process two")

def processThree(start):
    rand = random.random()
    time.sleep(rand)
    end = time.time()
    current = end - start
    print(str(current) + " process three")

if __name__ == "__main__":

    start = time.time()

    first_thread = threading.Thread(target=processOne, args=(start,))
    second_thread = threading.Thread(target=processTwo, args=(start,))
    third_thread = threading.Thread(target=processThree, args=(start,))

    first_thread.start()
    second_thread.start()
    third_thread.start()

    first_thread.join()
    second_thread.join()
    third_thread.join()


