# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)
# Input: 5
# Output: yes

def SimpleDig(dig):
    for i in range(2, dig):
        if dig % i == 0:
            return False
    return True

n = int(input('Введите число: '))
print(SimpleDig(n))

