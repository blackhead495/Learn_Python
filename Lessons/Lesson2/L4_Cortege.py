# Кортеж - это неизменяемый список

# t = ()
# print(type(t))              # typle - список
#
# t = (1, )
# print(type(t))              # typle
#
# t = (1)
# print(type(t))              # int
#
# t = (28, 9, 1990)
# print(type(t))              # typle
#
# colors = ['red', 'green', 'blue']
# print(colors)               # ['red', 'green', 'blue']
#
# t = tuple(colors)
# print(t)                    # ('red', 'green', 'blue')

#---------------------------------------------------------
# Доступ к элементам кортежа

# a = (3, 41, 15, 22)
# print(a)
# print(a[-1])
#
# for item in a:
#     print(item)

#---------------------------------------------------------
# Распаковка кортежа в отдельные переменные

t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue))
