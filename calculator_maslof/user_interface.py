
import compl
import model_sum
import model_sub
import model_mult
import model_div
import logg
import excep as ex
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
def number_type_selection():
    global a, b
    count = 0
    num = input('C каками числами будем работать:\n' '1.Рационалные;\n' '2.Комплексные.\n' '3.Завершение задачи.\n' 'Ввод: ')
    number()
    while count == 0:
        if num == 1:
            a = compl.get_value()
            b = compl.get_value()
            count = 1
        elif num == 2:
            a = compl.get_value_compl()
            b = compl.get_value_compl()
            count = 1
        elif num == 3:
            count = 1
            print('Задача завершена!')
    return a, b


def choosing_an_arithmetic_action(a, b):
    global c
    num_2 = input('Введите операцию над числами!\n' '+  - * / ^ q \n'  'Ввод: ')
    count = 0
    operands = '+-*/^q'
    while count == 0:
        for i in operands:
            if num_2 == operands[0]:
                model_sum.init(a, b)
                c = model_sum.do_it()
                count = 1
            elif num_2 == operands[1]:
                model_sub.init(a, b)
                c = model_sub.do_it()
                count = 1
            elif num_2 == operands[2]:
                model_mult.init(a, b)
                c = model_mult.do_it(a, b)
                count = 1
            elif num_2 == operands[3]:
                if b > 0:
                    model_div.init(a, b)
                    c = model_div.do_it()
                elif b == 0:
                    print('Делить на ноль нельзя!')
                    number_type_selection()
                count = 1
            elif num_2 != operands[0: 4] or num_2 == '' or num_2 == ' ':
                num_2 = input('Нукорректный ввод! Введите операцию над числами еще раз!\n' '+ - * / \n'  'Ввод действия: ')
                count = 0
    print(f'{a} {num_2} {b} = {c}')
    logg.input_logger(f'Выполненое действие: {a} {num_2} {b} = {c}')
    return c


def button_click():
    number_type_selection()
    choosing_an_arithmetic_action(a, b)
    result = c
    number_type_selection()