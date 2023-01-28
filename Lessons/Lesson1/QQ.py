# a = 123
# b = 1.23
# val = None
# print(type(a))
# print(type(b))
# val = 1266
# print(type(val))

# s = 'hello'
# print(s)    # Вывод строки
# print(a, '-', b,  '-', s)
# print('{} - {} - {}'.format(a, b, s))
# print(f'{a} - {b} - {s}')
# print('{1} - {2} - {0}'.format(a, b, s))

# f = True
# print(f)

# lst = [1, 2, 3]
# print(lst)
#
# lst = ['1', '2', '3', 'hello', 5.6]
# print(lst)

# print('Введите а')
# a = int(input())
# print('Введите b')
# b = int(input())
#
# print(a, b)
# print(a, ' + ', b, ' = ', a + b)

# print('Введите а')
# a = float(input())
# print('Введите b')
# b = float(input())
#
# print(a, b)
# print(a, ' + ', b, ' = ', a + b)

# Арифметические операции
# a = 1023
# b = 321
# c = a // b    # Деление с отбрасыванием остатка
# t = a % b     # Остаток от деления
# print(c)
# print(t)

# k = 1.31587
# m = 3
# n = round(k * m, 4)
#
# print(n)

# Логические операции
# t = 1 < 3 and 5 < 7
# print(t)
#
# a = [1, 2]
# b = [1, 2]
#
# print(a == b)

# f = 1 > 2 or 4 < 6
# print(f)

# f = [1, 2, 3, 4]
# print(not 2 in f)

# is_odd = not f[0] % 2
# print(is_odd)

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# Циклы

# original = int(input('original = '))
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + original % 10
#     original //= 10
#     print(original)
# else:
#     print('Пожалуй, хватит ')
#
# print(inverted)

# Управляющие конструкции

lst = [1, 2, 3, 4, 5]
for i in lst:
    print(i ** 2)

# r = range(10)
# for i in r:
#     print(i)
#
# for i in range(1, 10, 2):
#     print(i)
#
# for i in 'qwe-rty':
#     print(i)

# text = 'Съешь ещё этих мягких французских булок'
# print(text[0])              # С
# print(text[1])              # ъ
# print(len(text))            # 39
# print(text[len(text)-1])    # к
# print(text[-5])             # б
# print(text[:])              # print(text)
# print(text[:2])             # Съ
# print(text[6:-18])          # ещё этих мягких
# print(text[0:len(text):6])  # Сеикакл
# print(text[::6])            # Сеикакл

# Списки: введение
## list = list

# numbers = [1, 2, 3, 4, 5]
# print(numbers)
#
# ran = range(1, 6)
# numbers = list(ran)
# numbers[0] = 10
# print(numbers)
# print(f'len = {len(numbers)}')
# for i in numbers:
#     i *= 2
#     print(i)
# print(numbers)

colors = ['red', 'green', 'blue']

for e in colors:
    print(e)            # red green blue

for e in colors:
    print(e*2)          # redred greengreen blueblue

colors.append('gray')   # добавить в конец
print(colors)

colors.remove('red')    # del colores[0]  - удалить элемент
print(colors)

del colors[0]
print(colors)










