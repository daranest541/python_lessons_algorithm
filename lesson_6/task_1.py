# Задача №1 Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Python 3.6.0 64 bit

import sys

# Задача 5. Урок 2. Вывести таблицу символов ASCII от 32 до 127

ASCII_START = 32
ASCII_END = 127

# решение через while
print('решение через while')
ascii_table = ''
col_iter = 1
i = ASCII_START
while i <= ASCII_END:
    ascii_table += f'{i}-{chr(i)}'
    if col_iter % 10 == 0:
        ascii_table += '\n'
    col_iter += 1
    i += 1
print(f'ascii_table = {sys.getsizeof(ascii_table)} col_iter = {sys.getsizeof(col_iter)} i = {sys.getsizeof(i)} ASCII_START = {sys.getsizeof(ASCII_START)} ASCII_START = {sys.getsizeof(ASCII_END)}')
# ascii_table = 470 байт col_iter = 28 байт i = 28 ASCII_START = 28 байт ASCII_START = 28 байт

# вариант решения в одну строку через генератор
print('вариант решения в одну строку через генератор')
ascii_table = ''.join([f'{x}-{chr(x)}' + ('\n' if (i + 1) % 10 == 0 else '') for i, x in enumerate(range(ASCII_START, ASCII_END + 1))])

print(f'ascii_table = {sys.getsizeof(ascii_table)} i = {sys.getsizeof(i)} ASCII_START = {sys.getsizeof(ASCII_START)} ASCII_START = {sys.getsizeof(ASCII_END)}')
# ascii_table = 470 байт i = 28 ASCII_START байт = 28 байт ASCII_START = 28 байт
