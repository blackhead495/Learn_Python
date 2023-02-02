def fib(n):
    if n in [1, 2]:     # Если значение n равно одному из значений в списке
        return 1
    else:
        return fib(n-1) + fib(n-2)

lst = []
for e in range(1, 10):
    lst.append(fib(e))
print( *lst )
