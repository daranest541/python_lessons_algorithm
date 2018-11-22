# принтер графика
import os
import random
import time


clear = lambda: os.system('cls')


def rand_array(min_, max_):
    array = [i for i in range(min_, max_ + 1)]
    random.shuffle(array)
    return array


def print_graph(array, min_, max_, iteration, method_name, orig_array):
    clear()
    print(f'{method_name}, кол-во итераций:{iteration}')
    print(orig_array)
    # показываем график если диапазон меньше 50
    if max_ - min_ <= 50:
        while max_ > min_:
            row = ''
            for n in array:
                if n >= max_:
                    row += '▓'
                else:
                    row += '░'
            print(row)
            max_ -= 1
    print(array)
    time.sleep(0.25)


def print_help():
    print('arg1 - метод (bubble, merge, other)')
    print('arg2 - минимальное число массива')
    print('arg2 - максимальное число массива')