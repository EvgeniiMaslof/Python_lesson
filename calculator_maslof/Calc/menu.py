def type_of_numbers():
    print('Выбирите с какими числами будем работать. \n '
          '1. Рациональные.\n '
          '2. Комплексные.\n '
          '3. Завершить работу. ')


def type_of_operation():
    print(
        f'Выбирите операцию над числами.\n '
        '1. Сложение "+".\n '
        '2. Вычитание "-".\n '
        '3. Умножение "*".\n '
        '4. Деление "/".\n '
        '5. Возведение в степень "^".\n '
        '6. Квадратный корень "√"')


def number():
    num = input('Введите число: ')
    operand = '123'
    count = 0
    while count >= 1:
        if num == '' or num == ' ' or num not in operand or 0 >= int(num) >= 4:
            print('Неверный ввод')
            num = input('Введите число: ')
            count = 0
        else:
            count += 1
    return int(num)
        # elif int(num) == 3:
        #     count = 1


def znak():
    num = input('Введите число: ')
    operand = '123456'
    count = 0
    while count == 0:
        if num == '' or num == ' ' or num not in operand or 0 >= int(num) >= 7:
            print('Неверный ввод')
            num = input('Введите число: ')
        else:
            count = 1
            return (num)
    # return int(num)
# number()