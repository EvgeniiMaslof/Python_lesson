Position_one = int(input("Введите первое число:" ))
Position_two = int(input("Введите второе число:" ))
n = int(input('Введите N= '))
num = range(-n, n+1)
numbers = list(num)
print(numbers)
if Position_one <= len(numbers) >= Position_two:
     composition = numbers[Position_one - 1] * numbers[Position_two - 1]
     print(f"Произведение позиций {composition}")
else:
    print("Число вне диапазона списка!")
