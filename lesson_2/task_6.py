# Задача 6. Отгадать случайное число
# Блок-схемы 6 штук https://drive.google.com/file/d/1G6984wx68CYWY2DAVM5qm1JhSiZQHYi3/view?usp=sharing

import random

rand_num = random.randint(1, 100)
attempts = 0
status = 1

print('Компьютер загадал число, отгатайте его за 10 попыток')
while status == 1:
    if attempts < 10:
        user_num = int(input('Введите число: '))
        if user_num == rand_num:
            status = 2
        else:
            attempts += 1
            if user_num > rand_num:
                print('Ваше число больше загаданного')
            else:
                print('Ваше число меньше загаданного')
    else:
        status = 0
if status == 2:
    print(f'Вы отгадали число {rand_num}')
else:
    print(f'Вы исчерпали попытки, загаданное число {rand_num}')

