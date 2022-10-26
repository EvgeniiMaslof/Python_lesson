def fam():
    num_1 = input('Введите фамилию: ')
    count = 0
    while count == 0:
       if num_1 == '' or num_1 == ' ' or len(num_1) >= 10:
           num_1 = input('Ошибка ввода. Введите фамилию: ')
           count = 0
       else:
           count = 1
           return num_1

def name():
    num_2 = input('Введите имя: ')
    count = 0
    while count == 0:
       if num_2 == '' or num_2 == ' ' or len(num_2) >= 12:
           num_2 = input('Ошибка ввода. Введите имя: ')
           count = 0
       else:
           count = 1
           return num_2

def otch():
    num_3 = input('Введите отчество: ')
    count = 0
    while count == 0:
       if num_3 == '' or num_3 == ' ' or len(num_3) >= 17:
           num_3 = input('Ошибка ввода. Введите отчество: ')
           count = 0
       else:
           count = 1
           return num_3

def tel():
    num_4 = input('Введите номер телефона: ')
    count = 0
    while count == 0:
       if num_4 == '' or num_4 == ' ' or len(num_4) == 12:
           num_4 = input('Ошибка ввода. Введите номер телефона: ')
           count = 0
       else:
           count = 1
           return num_4