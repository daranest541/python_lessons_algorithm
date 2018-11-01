# Задача 1. калькулятор
# Блок-схемы 6 штук https://drive.google.com/file/d/1G6984wx68CYWY2DAVM5qm1JhSiZQHYi3/view?usp=sharing


while True:
    a = int(input('Введите первое число: '))
    op = input('Введите знак: ')
    b = int(input('Введите первое число: '))
    if op == '0':
        print('Отключаем')
        exit()
    elif op == '/':
        if b == 0:
            print('Деление на 0!!')
            continue
        else:
            res = a / b
    elif op == '+':
        res = a + b
    elif op == '-':
        res = a - b
    elif op == "*":
        res = b * b
    else:
        print(f'неизвестный оператор')
        continue
    print(f'Результат: {a}{op}{b} = {res}')
