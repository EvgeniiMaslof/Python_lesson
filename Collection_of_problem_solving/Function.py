# def concatenatio(*params): #передача неограниченного числа аргументов в функцию *
#     res: str = ""   # может быт и int =0 для работы с числами
#     for item in params:
#         res += item    # склеивание строк res
#     return res
#
# print(concatenatio('a', 'b', 'c', 'd')) #abcd
# print(concatenatio('a', 'b', 'c', 'd'))
# # print(concatenatio(1, 2, 3, 4))

# a = (3, 4)  # создается кортеж неизменяемый список, вывод данных кортежа по индексам
# print(a)
# print(a[0])
# print(a[1])
# for item in a:
#     print(item)

t = tuple(['red', 'green', 'blue']) # распаковка кортежа и присваивание каждому значению своей переменной
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue))
