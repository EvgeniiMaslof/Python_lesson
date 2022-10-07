# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input("Задайте натуральное число N: "))
count = 0
divider = []
while N != count:
    if N % 2 == 0:
        N = N // 2
        divider.append(2)
    elif N % 3 == 0:
        N= N // 3
        divider.append(3)
    elif N % 5 == 0:
        N= N // 5
        divider.append(5)
    elif  N != 0:
        divider.append(N)
        count = N
print(divider)