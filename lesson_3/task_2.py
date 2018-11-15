# Задача №2.
import random

SIZE = 10
array = [random.randint(0, SIZE * SIZE) for _ in range(SIZE)]
result_array = []
print(array)
for i in array:
    if i % 2 == 0:
        result_array.append(i)
print(result_array)
