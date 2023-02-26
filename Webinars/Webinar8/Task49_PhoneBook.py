# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

path = 'phonebook.txt'
def addPerson():                #  -- 1 --
    with open(path, 'a') as data:
        data.write(input('Введите фамилию: '))
        data.write(' ')
        data.write(input('Введите имя: '))
        data.write(' ')
        data.write(input('Введите отчество: '))
        data.write(' ')
        data.write(input('Введите номер телефона: '))
        data.write('\n')

def findPerson():               #  -- 2 --
    userRequest = input('Введите слово для поиска: ')
    count = 0
    with open(path, 'r') as data:
        for line in data:
            if userRequest in line:
                print(line, end='')
                count += 1
    if count == 0:
        print('Совпадений не найдено')

def replacePerson():            #  -- 3 --
    oldword = input('Введите слово, которое нужно изменить: ')
    newword = input('Введите слово, которым нужно заменить: ')
    count = 0
    pos = 0
    with open(path, "r") as data:
        L = data.readlines()
        for line in L:
            if oldword in line:
                count += 1
                print('Сделать изменение в записи - ', line, '?', end='')
                answer = input('Y - Да, N - Нет: ')
                if answer == 'Y' or answer == 'y':
                    L[pos] = line.replace(oldword, newword)
                    print(L[pos])
                    break
        pos += 1

    with open(path, "w") as data:
        for line in L:
            data.write(line)

    if count == 0:
        print('Совпадений не найдено')

def deletePerson():             #  -- 4 --
    userRequest = input('Введите слово для удаления записи: ')
    count = 0
    pos = 0

    with open(path, "r") as data:
        L = data.readlines()
        #print(L)
        for line in L:
            if userRequest in line:
                print(line, end='')
                answer = input('Удалить? Y - Да, N - Нет: ')
                if answer == 'Y' or answer == 'y':
                    print(pos)
                    count += 1
                    break
            pos += 1

        while pos < len(L) - 1:
            L[pos] = L[pos + 1]
            pos += 1
        L = L[:-1]  # убрать последний элемент в списке

        #print(L)

    with open(path, "w") as data:
        for line in L:
            data.write(line)

    if count == 0:
        print('Совпадений не найдено')

def printPhoneBook():           #  -- 5 --
    with open(path, 'r') as data:
        rdata = data.read()
    print(rdata)



def begin():
    #while True:
        print('1 - добавление новой записи')
        print('2 - поиск записи')
        print('3 - изменение записи')
        print('4 - удаление записи')
        print('5 - вывод всего списка')
        print('0 - выход')

        command = int(input('Введите пункт меню: '))

        match command:
            case 1:
                addPerson()
            case 2:
                findPerson()
            case 3:
                replacePerson()
            case 4:
                deletePerson()
            case 5:
                printPhoneBook()
            case _:
                print('До свидания!')
                exit()

#----------------------------------------------
begin()