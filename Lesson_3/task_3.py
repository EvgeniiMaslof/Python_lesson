# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000
#
# in
# 11
# out
# 1011
numbers = int(input("Введите число: "))
result = 0
count = 1
while numbers != 0:
    result = result + numbers % 2 * count
    numbers //= 2
    count *= 10
print(result)