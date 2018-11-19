# Задача 1 метод пузырька

from graph_printer import rand_array, print_graph, print_help
import sys


def bubble_sort(array, min_, max_):
    loop_n = 0
    orig_array = array.copy()
    for n in range(len(array) - 1, 0, -1):
        for i in range(n):
            loop_n += 1
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i+1], array[i]
        # Вдохновляясь этим видео https://youtu.be/kPRA0W1kECg я сделал визуализацию данного алгоритма
        # график рабоатет только на диапазоне до 50, если больше заезжает на другие строки
        print_graph(array, min_, max_, loop_n, 'Метод пузырька', orig_array)

# так как cls в pycharm не работает то запускать нужно через консоль, иначе не видна "анимация"))
# Вызов: python bubble 0 50
# где bubble - метод сортировки, 0 - минимальное значение, 50 - максимальное значение
if __name__ == "__main__":
    do = {
        "help": print_help,
        "bubble": bubble_sort
    }
    try:
        key, min_, max_ = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])

    except IndexError:
        print('index error')
        key, min_, max_ = None, None, None

    # key, min_, max_ = 'bubble', -10, 10
    if key:
        if do.get(key) and key is not None and max_ is not None and min_ is not None:
            array = rand_array(min_, max_)
            do[key](array, min_, max_)
        else:
            print("Задан неверный ключ")
            print("Укажите ключ help для получения справки")
