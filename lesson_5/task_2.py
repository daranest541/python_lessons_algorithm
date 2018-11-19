# Задача №2 сложение и умножение шестнадцатеричных чисел
from collections import deque
from collections import defaultdict

def get_num(position):
    while True:
        num = input(f"Введите {position} шестнадцатеричное число: ")
        for ch in num:
            if ch in '1234567890ABCDEFabcdef':
                return num.upper()
            else:
                print("Некорректный формат числа")
                break


def get_sign():
    while True:
        sign = input(f"Введите знак: ")
        if sign == "*" or sign == "+":
            return sign
        else:
            print("Некорректный знак")


# матрица сложения шестнадцатеричных чисел

hex_range = '0123456789ABCDEF'
nums_deque = deque([i for i in hex_range], maxlen=16)

matrix = defaultdict(dict)
offset = 0
for A in hex_range:
    column = defaultdict(list)
    if offset > 0:
        nums_deque.append(f'1{nums_deque[0]}')
    for idx, B in enumerate(hex_range):
        matrix[A][B] = nums_deque[idx]
    offset += 1

# print("\n".join([str("\t".join([str(col) + "+" + str(row) + ":" + str(matrix[row][col]) for col in matrix[row]])) for row in matrix]))


#сложение в столбик

def hex_sum(num1, num2, matrix):

    res = deque()
    rem = 0
    if len(num1) < len(num2):
        spam = num1
        num1 = num2
        num2 = spam
    num2_max_pos = len(num2) - 1
    num1, num2 = num1[::-1], num2[::-1]
    for pos, n in enumerate(num1):
        if pos <= num2_max_pos:
            tmp_res = matrix[num1[pos]][num2[pos]]
            if len(tmp_res) == 1 and rem == 0:
                res.appendleft(tmp_res[0])
            elif len(tmp_res) > 1 and rem == 0:
                res.appendleft(tmp_res[1])
                rem = 1
            elif len(tmp_res) > 1 and rem == 1:
                tmp_res = matrix[tmp_res[1]]["1"]
                if len(tmp_res) > 1:
                    res.appendleft(tmp_res[1])
                    rem = 1
                else:
                    res.appendleft(tmp_res[0])
                    rem = 0
            elif len(tmp_res) == 1 and rem == 1:
                tmp_res = matrix[tmp_res[0]]["1"]
                if len(tmp_res) > 1:
                    res.appendleft(tmp_res[1])
                    rem = 1
                else:
                    res.appendleft(tmp_res[0])
                    rem = 0
        else:
            if rem == 1:
                tmp_res = matrix[num1[pos]]["1"]
                if len(tmp_res) > 1:
                    res.appendleft(tmp_res[1])
                    rem = 1
                else:
                    res.appendleft(tmp_res[0])
                    rem = 0
            else:
                res.appendleft(num1[pos])
    return res


num1, sign, num2 = get_num(1), get_sign(), get_num(2)

# пока только сумму сделал, умножение по позже доделаю
print(hex_sum(num1, num2, matrix))