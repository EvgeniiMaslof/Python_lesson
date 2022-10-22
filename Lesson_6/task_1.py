# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения
# которых больше предыдущего элемента.
from random import randint


def random_list(number):
    result_list = [randint(0, 1000) for _ in range(number)]
    print(result_list)
    return [result_list[number] for number in range(1, len(result_list)) if result_list[number] > result_list[number - 1]]


print(random_list(int(input('Введите число: '))))
