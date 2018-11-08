# Задача 3. число обратное по порядку входящих в него цифр
# Блок-схемы 6 штук https://drive.google.com/file/d/1G6984wx68CYWY2DAVM5qm1JhSiZQHYi3/view?usp=sharing
num = int(input('Введите натуральное число: '))

if num == 0:
    print('Введенное число должно быть больше или меньше 0')
    exit()

num, result, length, i = abs(num), 0, len(str(num)), 1

while i <= length:
    print(num % 10)
    result += (num % 10) * (10 ** (length - i))
    num = int(num / 10)
    i += 1

print(f'Обратное число: {result}')
