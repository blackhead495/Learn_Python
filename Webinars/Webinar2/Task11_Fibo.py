# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.

# Input:     5
# Output:    6


ifibo = int(input('Введите число Фибоначчи : '))

fibo = 0
x1 = 1
x2 = 0
i = 1

while fibo < ifibo:
    fibo = x1 + x2
    x1 = x2
    x2 = fibo
    i += 1

if ifibo == fibo:
    print(i)
else:
    print(-1)


