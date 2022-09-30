n = int(input('Введите N= '))
num = range(-n, n+1)
numbers = list(num)
for i in numbers:
    print(i)
Position_one = int(input("Введите первое число:" ))
Position_two = int(input("Введите второе число:" ))
composition = numbers[Position_one - 1] * numbers[Position_two - 1]
print(composition)

