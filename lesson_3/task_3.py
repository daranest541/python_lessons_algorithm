# Задача №3.
import random

SIZE = 10
array = [random.randint(0, SIZE * SIZE) for _ in range(SIZE)]
print(array)

max_num = 0
min_num = array[0]

for i in array:
    if i > max_num:
        max_num = i
    if i < min_num:
        min_num = i
print(f'максимальное число {max_num}')
print(f'минимальное число {min_num}')
