# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
#
# out
# [2, 5, 8, 10]
# [20, 40]
#
# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]
import random

def form(numbers):
    array = random.sample(range(numbers * 2), numbers)
    print(array)
    return array
def composition(array):
    array2 = []
    i = 0
    for i in range(0, len(array)//2):
        array2.append(array[i] * array[-i-1])
    if len(array) % 2 != 0:
        array2.append(array[len(array)//2])
    print(array2)
numbers = int(input("Введите число: "))
composition(form(numbers))