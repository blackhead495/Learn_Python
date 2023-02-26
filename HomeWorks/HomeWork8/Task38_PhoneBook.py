# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

path = 'phonebook.txt'
def addPerson():                #  -- 1 --
    with open(path, 'a', encoding='UTF-8') as data:
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
    with open(path, 'r', encoding='UTF-8') as data:
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
    with open(path, "r", encoding='UTF-8') as data:
        L = data.readlines()
        for line in L:
            if oldword in line:
                count += 1
                print('Сделать изменение в записи -> ', line.strip(), '? ', end='')
                answer = input('Y - Да, N - Нет: ')
                if answer.upper() == 'Y':
                    L[pos] = line.replace(oldword, newword)
                    print('Запись изменена на ---------> ', L[pos])
                    break
        pos += 1

    if count == 0:
        print('Совпадений не найдено')
    else:
        with open(path, "w", encoding='UTF-8') as data:
            for line in L:
                data.write(line)

def deletePerson():             #  -- 4 --
    userRequest = input('Введите слово для удаления записи: ')
    count = 0
    pos = 0

    with open(path, "r", encoding='UTF-8') as data:
        L = data.readlines()
        #print(L)
        for line in L:
            if userRequest in line:
                print(line, end='')
                answer = input('Удалить? Y - Да, N - Нет: ')
                if answer.upper() == 'Y':
                    count += 1
                    break
            pos += 1

        while pos < len(L) - 1:
            L[pos] = L[pos + 1]
            pos += 1
        L = L[:-1]  # убрать последний элемент в списке

        #print(L)

    if count == 0:
        print('Совпадений не найдено')
    else:
        with open(path, "w", encoding='UTF-8') as data:
            for line in L:
                data.write(line)

def printPhoneBook():           #  -- 5 --
    with open(path, 'r', encoding='UTF-8') as data:
        rdata = data.read()
    print(rdata)


