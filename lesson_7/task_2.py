from graph_printer import rand_array
import sys


def merge_sort(array):
    arr = array.copy()
    len_ = len(array)
    if len_ >= 2:
        m = int(len_ // 2)
        left = merge_sort(arr[:m])
        right = merge_sort(arr[m:])
        arr = merge_move(left, right)
    return arr


def merge_move(l, r):
    new_arr = []
    while l and r:
        if l[0] < r[0]:
            new_arr.append(l.pop(0))
        else:
            new_arr.append(r.pop(0))
    if l:
        new_arr.extend(l)
    if r:
        new_arr.extend(r)
    return new_arr

if __name__ == "__main__":
    do = {
        #"help": print_help,
        "merge": merge_sort
    }
    try:
        key, min_, max_ = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])

    except IndexError:
        print('index error')
        key, min_, max_ = None, None, None

    # key, min_, max_ = 'merge', -10, 10
    if key:
        if do.get(key) and key is not None and max_ is not None and min_ is not None:
            array = rand_array(min_, max_)
            print(array)
            print(do[key](array))
        else:
            print("Задан неверный ключ")
            print("Укажите ключ help для получения справки")