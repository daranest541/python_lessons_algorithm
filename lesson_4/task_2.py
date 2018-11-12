# Задача №2. Алгоритм поиска простого числа
import cProfile

# эратосфен
def eratosthenes(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i
    res = [i for i in sieve if i != 0]
    return res
    # print(res)


# timeit "task_2.eratosthenes(10000)"
# 100 loops, best of 3: 3.68 msec per loop
# timeit "task_2.eratosthenes(20000)"
# 100 loops, best of 3: 7.69 msec per loop
# timeit "task_2.eratosthenes(50000)"
# 100 loops, best of 3: 19.8 msec per loop
# timeit  "task_2.eratosthenes(100000)"
# 100 loops, best of 3: 43.2 msec per loop


# cProfile.run('eratosthenes(10000)')  1    0.003    0.003    0.004    0.004 task_2.py:5(eratosthenes)
# cProfile.run('eratosthenes(20000)')  1    0.007    0.007    0.008    0.008 task_2.py:5(eratosthenes)
# cProfile.run('eratosthenes(50000)')  1    0.019    0.019    0.023    0.023 task_2.py:5(eratosthenes)
# cProfile.run('eratosthenes(100000)') 1    0.039    0.039    0.048    0.048 task_2.py:5(eratosthenes)


def my_prime(n):
    res = []
    for j in range(2, n):
        is_prime = True
        for i in range(2, j):
            if j % i == 0:
                is_prime = False
        if is_prime:
            res.append(j)
    # print(res)
    return res

# timeit "task_2.my_prime(1000)"
# 10 loops, best of 3: 33.1 msec per loop
# timeit "task_2.my_prime(2000)"
# 10 loops, best of 3: 145 msec per loop
# timeit "task_2.my_prime(5000)"
# 10 loops, best of 3: 1 sec per loop

# cProfile.run('my_prime(1000)')  1    0.047    0.047    0.047    0.047 task_2.py:35(my_prime)
# cProfile.run('my_prime(2000)')  1    0.164    0.164    0.164    0.164 task_2.py:35(my_prime)
# cProfile.run('my_prime(5000)')  1    0.977    0.977    0.977    0.977 task_2.py:35(my_prime)

