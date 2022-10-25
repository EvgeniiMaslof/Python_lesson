import menu as m
import here_is_the_data as hit
import model_sum as s
import model_sub as sub
import model_mult as mult
import model_div as div
import model_exponentiation as exp
import model_square_root as sq
import logg


def choosing_an_arithmetic_action(a, b):
    global c
    num_2 = input('Введите операцию над числами!\n' '+  - * / ^ q \n'  'Ввод: ')
    count = 0
    operands = '+-*/^q'
    while count == 0:
        for i in operands:
            if num_2 == operands[0]:
                s.init(a, b)
                c = s.do_it()
                count = 1
            elif num_2 == operands[1]:
                sub.init(a, b)
                c = sub.do_it()
                count = 1
            elif num_2 == operands[2]:
                mult.init(a, b)
                c = mult.do_it()
                count = 1
            elif num_2 == operands[3]:
                if b > 0:
                    div.init(a, b)
                    c = div.do_it()
                elif b == 0:
                    print('Делить на ноль нельзя!')
                    number_type_selection()
                count = 1
            elif num_2 == operands[4]:
                exp.init(a, b)
                c = exp.do_it()
                count = 1
            elif num_2 == operands[5]:
                sq.init(a)
                c = sq.do_it()
                count = 1
            elif num_2 != operands[0: 5] or num_2 == '' or num_2 == ' ':
                num_2 = input('Нукорректный ввод! Введите операцию над числами еще раз!\n' '+ - * / \n'  'Ввод действия: ')
                count = 0
    print(f'{a} {num_2} {b} = {c}')
    logg.input_logger(f'{a} {num_2} {b} = {c}')

def action():
    num_2 = input('Введите число: ')
    operand = '123456'
    count = 0
    while count == 0:
        if num_2 == '' or num_2 == ' ' or num_2 not in operand or 0 >= int(num_2) >= 7:
            print('Неверный ввод')
            num_2 = input('Введите число: ')
        else:
            count = 1
            return int(num_2)

m.type_of_numbers()
num = input('Введите число: ')
operand = '123'
count = 0
a = 0
b = 0
c = 0
while count == 0:
    if num == '' or num == ' ' or num not in operand or 0 >= int(num) >= 4:
        print('Неверный ввод')
        num = input('Введите число: ')
        count = 0
    else:
        count += 1
        # print(num)
if int(num) <= 1:
    a = float(hit.get_value())
    b = float(hit.get_value())
elif int(num) == 2:
    a = hit.get_value_compl()
    b = hit.get_value_compl()
elif int(num) == 3:
    print('Завершение работы!')
choosing_an_arithmetic_action(a, b)

# if int(num_3) == 1:
#     s.init(a, b)
#     c = s.do_it()
# elif int(num_3) == 2:
#     sub.init(a, b)
#     c = sub.do_it()
# elif int(num_3) == 3:
#     mult.init(a, b)
#     c = mult.do_it()
# elif int(num_3) == 4:
#     div.init(a, b)
#     c = div.do_it()
# elif int(num_3) == 5:
#     exp.init(a, b)
#     c = exp.do_it()
# elif int(num_3) == 6:
#     sq.init(a)
#     c = sq.do_it()
# print(f'{a}  {b} = {c}')
# logg.input_logger(f'Выполненое действие: {a}  {b} = {c}')