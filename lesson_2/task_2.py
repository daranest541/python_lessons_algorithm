# Задача 2. посчитать количество четных и нечетных

num = int(input('Введите натуральное число: '))

if num == 0:
    print('Введенное число должно быть больше или меньше 0')
    exit()
num = abs(num)
even = 0
odd = 0
length = len(str(num))
i = 0

while i < length:
    if num % 10 % 2 == 0:
        print(f'Цифра {num % 10} четная')
        even += 1
    else:
        print(f'Цифра {num % 10} нечетная')
        odd += 1
    num = int(num / 10)
    i += 1

print(f'Итого: четных {even}, нечетных {odd}')
