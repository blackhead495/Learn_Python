# import hello    # Использовать данные и функции из файла hello.py
# print(hello.f(1))

# import hello as h       # Использовать h как псевдоним файла hello.py
# print(h.f(1))

#----------------------------------------------
#--- Значение параметров по умолчанию ---------
# def new_string(symbol, count = 3):
#     return symbol * count
#
# print(new_string('!', 5))       # !!!!!
# print(new_string('!'))          # !!!
# print(new_string(4))            # 12

#-----------------------------------------------
#--- Неограниченное количество аргументов ------

def concatinatio(*params):
    res: str = ""
    for item in params:
        res += item
    return  res

print(concatinatio('a', 's', 'd', 'w'))         # asdw
print(concatinatio('a', '1', 'd', '2'))         # a1d2
# print(concatinatio(1, 2, 3, 4))               # TypeError
