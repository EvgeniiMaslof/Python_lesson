

def get_value():
    return float(input('Введите число: '))


def get_value_compl():
    value_complex = complex(get_value(), get_value())
    print(value_complex)
    return value_complex


def view_data(data, title):
    print(f'{title} = {data}')

