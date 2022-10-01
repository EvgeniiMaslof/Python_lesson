# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4

# out
# [4, 2, 4, 9]
# 8
import random


def form(numbers):
    array = random.sample(range(numbers * 2), numbers)
    print(array)
    return array

def summa(array):
    result = 0
    count = 0
    for i in len(array):
        if count <= len(array):
            result = result + array[count]
            count += 2
    print(result)

numbers = int(input())
form(numbers)
summa(array)
