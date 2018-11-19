# Задача №1 прибыль предприятий

from collections import Counter
from collections import namedtuple
from collections import defaultdict

Profit_class = namedtuple("Profit_class", "quarter1, quarter2, quarter3, quarter4")

profit = defaultdict(Profit_class)


year_profit = Counter()
total_profit = 0
num = int(input("Введите данны о количестве предприятий: "))
for i in range(num):
    name = input(f"Введите наименование {i + 1} предприятия: ")
    spam_profit = []
    for q in range(4):
        spam_quarter = int(input(f"Введите прибыль предприятия {name} за {q + 1} квартал: "))
        spam_profit.append(spam_quarter)
        year_profit[name] += spam_quarter
    total_profit += year_profit[name]
    profit[name] = Profit_class(spam_profit[0], spam_profit[1], spam_profit[2], spam_profit[3])


middle = total_profit / len(profit)
print(f"Средняя прибыль всех предприятий: {middle}")
print("Годовая прибыль ниже среднего: ")
for firm in year_profit:
    if year_profit[firm] < middle:
        print(f'Фирма: {firm}, Прибыль: {year_profit[firm]}')

print("Годовая прибыль выше среднего: ")
for firm in year_profit:
    if year_profit[firm] > middle:
        print(f'Фирма: {firm}, Прибыль: {year_profit[firm]}')

