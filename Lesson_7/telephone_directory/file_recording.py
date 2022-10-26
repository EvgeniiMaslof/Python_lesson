def telefon_csv(a, b, c, d):
    file = 'Phonebook.csv'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'{a}  {b}  {c}   Номер телефона: {d} \n')

def telefon_txt(a, b, c, d):
    file = 'Phonebook.txt'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'{a}  {b}  {c}   Номер телефона: {d} \n')


def telefon_2():
    file = 'Phonebook.txt'
    with open(file, 'r', encoding='utf-8') as data:
        txt = data.read()
        print(txt)