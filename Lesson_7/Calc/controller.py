import menu as m
import racion
import complex
import logg


def logic():
    m.type_of_numbers()
    num = input('Введите число: ')
    operand = '123'
    count = 0
    while count == 0:
        if num == '' or num == ' ' or num not in operand or 0 >= int(num) >= 4:
            print('Неверный ввод')
            num = input('Введите число: ')
            count = 0
        else:
            count += 1
    if int(num) <= 1:
        racio_action()
    elif int(num) == 2:
        complex_action()
    elif int(num) == 3:
        print('Завершение работы!')

def racio_action():
    a = 0
    b = 0
    c = 0
    m.type_of_operation()
    num_2 = input('Введите число: ')
    operand = '123456'
    count = 0
    while count == 0:
        if num_2 == '' or num_2 == ' ' or num_2 not in operand or 0 >= int(num_2) >= 7:
            print('Неверный ввод')
            num_2 = input('Введите число: ')
        else:
            count = 1
    if int(num_2) == 1:
        c = racion.sum()
    elif int(num_2) == 2:
        c = racion.sub()
    elif int(num_2) == 3:
        c = racion.mult()
    elif int(num_2) == 4:
        c = racion.div()
    elif int(num_2) == 5:
        c = racion.expo()
    elif int(num_2) == 6:
        c = racion.sq()
    logg.input_logger(c)
    print(c)

def complex_action():
    a = 0
    b = 0
    c = 0
    m.type_of_operation()
    num_2 = input('Введите число: ')
    operand = '12345'
    count = 0
    while count == 0:
        if num_2 == '' or num_2 == ' ' or num_2 not in operand or 0 >= int(num_2) >= 6:
            print('Неверный ввод')
            num_2 = input('Введите число: ')
        else:
            count = 1
    if int(num_2) == 1:
        c = complex.sum()
    elif int(num_2) == 2:
        c = complex.sub()
    elif int(num_2) == 3:
        c = complex.mult()
    elif int(num_2) == 4:
        c = complex.div()
    elif int(num_2) == 5:
        c = complex.expo()
    # elif int(num_2) == 6:
    #     c = complex.sq()
    #     d = '√'
    logg.input_logger(c)
    print(c)

def main():
    print('Привет я живой')
    logic()