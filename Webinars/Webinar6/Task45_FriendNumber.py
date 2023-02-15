# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число k, не превосходящее 10 в 5 степени.
# Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k.
# Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую пару не дает).
# Ввод:                     Вывод:
# 300                       220 284


#N = int(input('N: ')) # Максимальное число

# lsT_fr1 = []
# lst_fr2 = []
#
# sum_fr1 = 0
# sum_fr2 = 0
#
# for i in range(1, N):
#     for j in range(i, N):       # Поиск делителей 1
#         if N % j == 0:
#             lsT_fr1.append(i)
#
#     sum_fr1 = sum(lsT_fr1)
#
#     for k in range(j+1, N-1):
#         for l in range(k, N):
#             if N % k == 0:
#                 lst_fr2.append(i)
#             sum_fr2 = sum(lst_fr2)
#             if sum_fr1 == sum_fr2:
#                 lst_fr1.append(k)
#
# for m in range(len(lsT_fr1)):
#     print(lsT_fr1[m])
#
#
#
#
#
# print(lsT_fr1)
# print(sum_fr1)

import time

t_start = time.time()
result = []
for num in range(2, 1000001):
    sd_num = 1
    i = 2
    while (i * i <= num):
        (p, q) = divmod(num, i)
        if q == 0:
            sd_num += i
            if p != i:
                sd_num += p
        i = i + 1
    mun = sd_num
    sd_mun = 1
    i = 2
    while (i * i <= mun):
        (p, q) = divmod(mun, i)
        if q == 0:
            sd_mun += i
            if p != i:
                sd_mun += p
        i = i + 1
    if num == sd_mun and mun == sd_num:
        if (num != mun) and (num < mun):
            result.append((num, mun))
print(result)

t_fin = time.time()
print(t_fin - t_start)





