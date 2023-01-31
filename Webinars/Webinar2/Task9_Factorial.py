# По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while
# Input:       5
# Output:    120

num = int(input('Введите неотрицательное число : '))
n = num

fact = 1
while n > 1:
    fact *= n
    n -= 1

print(f'{num}! = {fact}')

fact = 1
n = num
for i in range(1, n+1):
    fact *= i

print(f'{num}! = {fact}')