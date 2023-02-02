# Как работать с файлами:
# Связать файловую переменную с файлом, определив модификатор работы
#  a - открытие для добавления данных
#  r - открытие для чтения данных
#  w - открытие для записи данных (старые данные удаляются)
#  w+ , r+ -


# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors)     # разделителей не будет
# data.close()
#
# with open('file.txt', 'w') as data:     # переменная data в дальнейшем выступает вместо file.txt
#     data.write('line 11\n')
#     data.write('line 23\n')


# exit()  # Разрешает не выполняться оставшейся части программы

path = 'file.txt'
data = open(path, 'r')   # Открываем файл для чтения
for line in data:
    print(line)
data.close()

