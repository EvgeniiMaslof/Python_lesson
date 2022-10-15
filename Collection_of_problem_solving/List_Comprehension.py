# list = []
# for i in range(1, 101):
#     if(i%2 == 0):
#         list.append(i)
# print(list)
# def f(x):
#     return x**3
#
# list = [f(i) for i in range(1, 20) if i%2 == 0]
# print(list)
# list = [1, 2, 3, 5, 8, 15, 23, 38]
# list1 = [(i, (i**2)) for i in list if not i%2]
# print(list1)
# path = 'file.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# f.close()
#
# numbers =[]
# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]
#
# out = [(i, (i**2)) for i in numbers if not i%2]
# print(out)
# li = [x for x in range(1, 21)]
# li = list(map(lambda x: x+10, li))
# print(li)

# data = list(map(int, input().split()))
# print(data)

list1 = [x for x in range(10)]
print(list1)
res = list(filter(lambda x: not x%2, list1))
print(res)

