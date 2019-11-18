import random

def n_in_pool(n, low, high):

    pool = random.choices(range(low, high), k=15)
    pool.sort()
    print(pool)
    found = False
    while not found and len(pool) > 1:
        middle = pool[len(pool)//2]
        if n > middle:
            del pool[:pool.index(middle)]
        elif n < middle:
            del pool[pool.index(middle):]
        elif n == middle:
            found = True
            break
    
    print(n, "in pool:", found)

n_in_pool(30, 10, 50)
n_in_pool(40, 10, 90)
n_in_pool(21, 1, 50)


    