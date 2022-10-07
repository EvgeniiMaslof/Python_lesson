# Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000

from decimal import Decimal

a = input("Введите число: ")
d = input("Укажите точность в диапазоне: " )
float_lst = Decimal(a)
float_lst = float_lst.quantize(Decimal(d))
print(float_lst)