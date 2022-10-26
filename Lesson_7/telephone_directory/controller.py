import data_entry as d
import menu as m
import recording_files as r


def logik():
    num = input('Введите номер пункта меню: ')
    count = 0
    hop = '123'
    while count == 0:
        if num == '' or num == ' ' or num not in hop or int(num) >= 4 or int(num) <= 0:
            num = input('Введено неверное значение. Повторите ввод номера пункта меню: ')
            count = 0
        elif int(num) == 1:
            r.telefon_csv(d.fam(), d.name(), d.otch(), d.tel())
            r.telefon_txt(d.fam(), d.name(), d.otch(), d.tel())
            count = 1
        elif int(num) == 2:
            r.telefon_2()
            count = 1
        elif int(num) == 3:
            print('Завершение работы')
            count = 1

def main_action():
    m.greeting()
    logik()