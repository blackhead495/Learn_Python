# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

import random

num_coins = int(input('Введите количество монет : '))
num_eagle = random.randint(1, num_coins)
num_tails = num_coins - num_eagle

if num_tails < num_eagle:
    min_coins = num_tails
else:
    min_coins = num_eagle

print(f'Из нах повернуты орлом : {num_eagle}')
print(f'Нужно перевернуть монет минимум : {min_coins}')
