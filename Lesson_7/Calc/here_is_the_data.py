def get_value():
    num = input('Введите значение числа: ')
    count = 0
    while count == 0:
        if num == '' or num == ' ' or num.isdigit() != True:
             print('Неверно ввели число, попробуйте еще раз!')
             num = input('Введите значение числа: ')
             count = 0
        else:
             count = 1
             return float(num)



def get_value_compl():
    value_complex = complex(get_value(), get_value())
    return value_complex

