# Задача №1 Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Python 3.6.0 64 bit

# Задача №3. Урок 3.

import random
import sys


def func_min_max(size, _range):
    array = [random.randint(_range[0], _range[1]) for _ in range(size)]
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
    print(sys.getsizeof(array) + sys.getsizeof(max_num_idx) + sys.getsizeof(min_num_idx) + sys.getsizeof(max_num) + sys.getsizeof(min_num))
    print(f'{sys.getsizeof(array)} + {sys.getsizeof(max_num_idx)} + {sys.getsizeof(min_num_idx)} + {sys.getsizeof(max_num)} + {sys.getsizeof(min_num)}')


func_min_max(1000, [-1000, 1000])

# программа занимает 9164 байт
# array = 9024,  max_num_idx = 28, min_num_idx = 28, max_num = 28, min_num = 28, idx = 28
