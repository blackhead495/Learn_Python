from Task38_PhoneBook import addPerson
from Task38_PhoneBook import findPerson
from Task38_PhoneBook import replacePerson
from Task38_PhoneBook import deletePerson
from Task38_PhoneBook import printPhoneBook

#import Task38_PhoneBook as t

def begin():
    #while True:
        print('\nГлавное меню:')
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