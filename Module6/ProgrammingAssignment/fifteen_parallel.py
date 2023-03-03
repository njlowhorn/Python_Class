# Python V 3.9.0

import multiprocessing as mp
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
    cores = mp.Pool(mp.cpu_count())

    start = time.time()

    firstResult = cores.apply(processOne, [start])
    secondResult = cores.apply(processTwo, [start])
    thirdResult = cores.apply(processThree, [start])



