#  Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
#  Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
#  В последующих  строках записаны N целых чисел Ai.
#  Последняя строка содержит число X
#   5
#   1 2 3 4 5
#   6
#   -> 5


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
near = 1000    # самое ближнее расстояние
count = 0
for i in range(n):
    tmp = abs(A[i] - X)
    if near > tmp:
        near = tmp
        count = i

print('->', A[count])


