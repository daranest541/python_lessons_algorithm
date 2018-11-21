# Задача 1 определить количество подстрок в строке

import string
import random

length = 100
istr = ''.join(random.choices(string.ascii_lowercase, k=length))
print(istr)

subs_set = set()
subs_set_str = set()
for i in range(1, length):
    k = length - i + 1
    for j in range(0, k):
        spam_substr = istr[j:i + j]
        subs_set.add(hash(spam_substr))


print(f'количество подстрок в строке = {len(subs_set)}')


