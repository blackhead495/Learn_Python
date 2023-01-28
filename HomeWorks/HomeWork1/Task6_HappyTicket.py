# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
# которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

n = int(input('Введите номер билета : '))

if 100000 <= n < 1000000:
    tmp = n
    Summa = [0, 0]

    for i in range(2):
        for j in range(3):
            d = tmp - tmp // 10 * 10
            Summa[i] += d
            tmp //= 10

    if Summa[0] == Summa[1]:
        print(f'{n} -> yes')
    else:
        print(f'{n} -> no')

else:
    print('Указан неверный номер билета...')