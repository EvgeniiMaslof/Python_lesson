import data_entry as d
import file_recording as f
import menu as m


def logik():
    num = input('Введите номер пункта меню: ')
    count = 0
    hop = '123'
    while count == 0:
        if num == '' or num == ' ' or num not in hop or int(num) >= 4 or int(num) <= 0:
            num = input('Введено неверное значение. Повторите ввод номера пункта меню: ')
            count = 0
        elif int(num) == 1:
            f.telefon_csv(d.fam(), d.name(), d.otch(), d.tel())
            f.telefon_txt(d.fam(), d.name(), d.otch(), d.tel())
            count = 1
        elif int(num) == 2:
            f.telefon_2()
            count = 1
        elif int(num) == 3:
            print('Завершение работы')
            count = 1

def start():
    m.mini_menu()
    logik()