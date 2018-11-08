# Задача 4. Найти сумму n элементов(1 + -0,5 + 0,25..)
# Блок-схемы 6 штук https://drive.google.com/file/d/1G6984wx68CYWY2DAVM5qm1JhSiZQHYi3/view?usp=sharing

n = int(input('Введите n: '))

if n <= 1:
    print('n должно быть больше 1')
    exit()

op, i, summ = 1, 0, 1
while n - 1 > i:
    if i % 2 == 0:
        op = 0 - op / 2
    else:
        op = abs(op / 2)
    # print(f'iter {i + 1} op {op}')
    summ = summ + op
    i += 1

print(f'сумма ряда равна {summ}')
