# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

import random
from array import array

n = int(input('Введите количество чисел в массиве: '))
A = array('i', )

for i in range(n):
    A.append((random.randint(1, 20)))

print('A = (', end='')
for i in range(len(A)):
    print(A[i], end=', ')
print('\b\b)')

X = int(input('Введите число для поиска: '))

count = 0
for i in range(n):
    if A[i] == X:
        count += 1

print('-> {} раз'.format(count))
