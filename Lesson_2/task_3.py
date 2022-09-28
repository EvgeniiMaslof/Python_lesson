def func(num):
    if num == 0:
        return 0
    return (1+1/num)**num + func(num-1)


n = int(input('Введите N= '))
result = {}
for i in range(1, n+1):
    result[i] = round(func(i), 0)
print(result)