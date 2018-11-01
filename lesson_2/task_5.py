# Задача 5. Вывести таблицу символов ASCII от 32 до 127

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
print(ascii_table)
# вариант решения в одну строку через генератор
print('вариант решения в одну строку через генератор')
ascii_table = ''.join([f'{x}-{chr(x)}' + ('\n' if (i + 1) % 10 == 0 else '') for i, x in enumerate(range(ASCII_START, ASCII_END + 1))])
print(ascii_table)

