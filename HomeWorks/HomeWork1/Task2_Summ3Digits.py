# Найдите сумму цифр трехзначного числа.
#       123 -> 6 (1 + 2 + 3)
#       100 -> 1 (1 + 0 + 0)

# ------ Способ 1 ----------------------------------------

# tmp = num = int(input('Введите трёхзначное число : '))
#
# d1 = tmp - tmp // 10 * 10
# tmp //= 10
# d2 = tmp - tmp // 10 * 10
# tmp //= 10
# d3 = tmp - tmp // 10 * 10
# tmp //= 10
#
# # print(num, '->', d1 + d2 + d3, '(', d3, '+', d2, '+', d1, ')')
# print(f'{num} -> {d1 + d2 + d3} ({d3} + {d2} + {d1})')

# ------- Способ 2 ------------------------------------

tmp = num = int(input('Введите трёхзначное число : '))
summa = 0
lst = []

while tmp:
    d = tmp - tmp // 10 * 10
    lst.append(d)
    summa += d
    tmp //= 10

lst.reverse()

print(num, '->', summa, '(', *lst, ')')

# print(f'{num} -> {summa} ( ', end='')
# for i in range(len(lst)):
#     print(lst[i], end=' ')
# else:
#     print(')')



