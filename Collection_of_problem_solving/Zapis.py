from random import choise

def poly_sum(name_1: str, name_2: str):
    with open(name_1, 'r', encoding='utf-8') as my_f_1, \
        open(name_2, 'r', encoding='unf-8') as my_f_2:
    first = my_f_1.readline()
    second = my_f_2.readline()

    if len(first) == len(second):
        with open('sum_poly.txt', 'a', encoding='utf-8') as my_f_3:
            for i, v in enumerate(first):
                my_f_3.write(f'{v[:-5]} + {second[i]}')
            else:
                print('The content of the files do not match!')

poly_sum('poly.txt', 'poly_2.txt')
