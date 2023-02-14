# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input:    2 -> 3 4
# Output: 4 3

n = int(input('Введите количество оценок: '))

def revers(k):
    if k == 0:
        return ""
    num = int(input())
    return revers(k-1) + f" {num}"

print(revers(n))