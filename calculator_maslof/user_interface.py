
import compl
import model_sum
import model_sub
import model_mult
import model_div
import logg

def number_type_selection():
    global a, b
    count = 0
    num = int(input('C каками числами будем работать:\n' '1.Рационалные;\n' '2.Комплексные.\n' '3.Завершение задачи.\n' 'Ввод: '))
    while count == 0:
        if num != 1 and num != 2 and num != 3:
            num = int(input('Некорректный ввод! Введите 1 или 2.\n' 'Ввод: '))
            count = 0
        elif num == 1:
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
    num_2 = input('Введите операцию над числами!\n' '+  - * / \n'  'Ввод: ')
    count = 0
    operands = '+ - * /'
    while count == 0:
        for i in operands:
            if num_2[0] == operands[0]:
                model_sum.init(a, b)
                c = model_sum.do_it()
                count = 1
            elif num_2[0] == operands[2]:
                model_sub.init(a, b)
                c = model_sub.do_it()
                count = 1
            elif num_2[0] == operands[4]:
                model_mult.init(a, b)
                c = model_mult.do_it(a, b)
                count = 1
            elif num_2[0] == operands[6]:
                model_div.init(a, b)
                c = model_div.do_it()
                count = 1
            elif num_2[0] != operands[0]:
                num_2 = input('Нукорректный ввод! Введите операцию над числами еще раз!\n' '+  - * / \n'  'Ввод действия: ')
                count = 0

        print(f'{a} {num_2} {b} = {c}')
    return c


def button_click():
    number_type_selection()
    choosing_an_arithmetic_action(a, b)
    result = c
    logg.view_data(result)