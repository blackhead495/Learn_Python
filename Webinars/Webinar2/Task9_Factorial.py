

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