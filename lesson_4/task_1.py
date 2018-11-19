# Задача №1.  Задача №3. из 3 урока
import random
import cProfile


def func_min_max(size, _range):
    array = [random.randint(_range[0], _range[1]) for _ in range(size)]
    # array = [-818, -339, -286, -922, -623, -445, -850, -459, -908, -832]
    # print(array)
    max_num_idx = 0
    min_num_idx = 0
    max_num = array[len(array) - 1]
    min_num = array[0]

    for idx, i in enumerate(array):
        if i > max_num:
            max_num = i
            max_num_idx = idx
        if i < min_num:
            min_num = i
            min_num_idx = idx
    array[min_num_idx] = max_num
    array[max_num_idx] = min_num
    # print(f'максимальное число {max_num}')
    # print(f'минимальное число {min_num}')

# timeit "task_1.func_min_max(100,[-1000, 1000])"
# 100 loops, best of 3: 1.46 msec per loop
# timeit "task_1.func_min_max(2000,[-1000, 1000])"
# 100 loops, best of 3: 2.98 msec per loop
# timeit "task_1.func_min_max(5000,[-1000, 1000])"
# 100 loops, best of 3: 7.35 msec per loop

# cProfile.run('func_min_max(10000,[-1000, 1000])') 10000    0.007    0.000    0.015    0.000 random.py:174(randrange)
# cProfile.run('func_min_max(100000,[-1000, 1000])') 100000    0.081    0.000    0.163    0.000 random.py:174(randrange)
# cProfile.run('func_min_max(1000000,[-1000, 1000])') 1000000    0.745    0.000    1.487    0.000 random.py:174(randrange)