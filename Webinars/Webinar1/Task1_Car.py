# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

# n = 700
n = int(input("Введите расстояние в день : "))
# m = 750
m = int(input("Введите общее расстояние : "))

print("Ответ :", ((m - 1) // n ) + 1)
