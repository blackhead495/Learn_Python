# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример 10: 1, 2, 3

num = int(input('Введите число : '))

i = 0       # Степень
p = 1       # Число равное 2^i
lst = []

while p <= num:
    p *= 2
    i += 1
    lst.append(i)

print(f'{num}: ', end='')

for i in range(len(lst)-1):
    print(f'{lst[i]}, ', end='')
else:
    print('\b\b')   # Стереть последнюю запятую

