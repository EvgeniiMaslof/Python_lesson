number = ''.join(input('Введите вещественное число ').split('.'))
sum = 0
for i in number:
    sum += int(i)
print(sum)