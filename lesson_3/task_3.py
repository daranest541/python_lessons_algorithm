# Задача №3.
import random

SIZE = 10
array = [random.randint(0, SIZE * SIZE) for _ in range(SIZE)]
print(array)
max_num_idx = 0
min_num_idx = 0
max_num = 0
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

print(array)

print(f'максимальное число {max_num}')
print(f'минимальное число {min_num}')


