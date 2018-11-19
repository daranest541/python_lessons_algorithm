# Задача №1 Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Python 3.6.0 64 bit

# Задача №2. Урок 3. _

import random
import sys

SIZE = 10
array = [random.randint(0, SIZE * SIZE) for _ in range(SIZE)]
result_array = []
# print(array)
for i in array:
    if i % 2 == 0:
        result_array.append(i)
# print(result_array)

print(sys.getsizeof(array))
print(sys.getsizeof(result_array))
# Программа занимает в памяти 900 байт
# SIZE: 28,  i: 28, array = 92, элементы array = 28 * 10 = 280, result_array = 192, элементы result_array = 28 * 10 = 280
