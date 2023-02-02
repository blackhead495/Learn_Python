# Множества

# colors = {'red', 'green', 'blue'}
# print(colors)           # {'red', 'green', 'blue'}
# print(type(colors))     # set
#
# colors.add('gray')    # добавить элемент
# print(colors)           # {'red', 'green', 'blue', 'gray'}
#
# colors.remove('red')
# print(colors)           # {'green', 'blue', 'gray'}
#
# colors.remove('red')    # KeyError: 'red' - нельзя удалять один элемент дважды
#
# colors.discard('red')   # А вот так уже можно удалять повторно
#
# colors.clear()          # Очистка множества

#---------------------------------------------------------------------------------
#--- Операции с множествами ------------------------------------------------------

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()                #   c = {1, 2, 3, 5, 8}         - Копирование
u = a.union(b)              #   u = {1, 2, 3, 5, 8, 13, 21} - Объединение
i = a.intersection(b)       #   i = {2, 5, 8}               - Пересечение
dl = a.difference(b)        #   dl = {1, 3}
dr = b.difference(a)        #   dr = {13, 21}
q = a.union(b).difference(a.intersection(b))
                            #   q  = {1, 21, 3, 13}

#---------------------------------------------------------------------------------
#--- Замороженные множества - их нельзя изменять ---------------------------------

s = frozenset(a)