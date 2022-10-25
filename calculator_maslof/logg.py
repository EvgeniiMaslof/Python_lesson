from datetime import datetime as dt


def view_data(result):

    with open('logg.csv', 'a') as file:
        file.write(f'{result}\n')
#
#

def input_logger(data):
    time = dt.now().strftime('%D  %H:%M')
    with open('logg.csv', 'a', encoding='utf-8') as file:
        file.write(f'{data}, {time} \n')