# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот:
# все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

import random

n = int(input('Введите количество оценок: '))
Z = []   # Оценки

for i in range(n):
    Z.append(random.randint(1, 5))

kmax = max(Z)
kmin = min(Z)

print(Z)
print(kmax, kmin)

for i in range(n):
    if Z[i] == kmax:
        Z[i] = kmin

print(Z)