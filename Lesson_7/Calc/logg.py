from datetime import datetime as dt


def input_logger(data):
    time = dt.now().strftime('%D  %H:%M')
    with open('logg.csv', 'a', encoding='utf-8') as file:
        file.write(f'{data}, {time} \n')