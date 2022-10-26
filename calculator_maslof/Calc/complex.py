import math
import here_is_the_data as hit


def init(a, b):
    global x
    global y
    x = a
    y = b

def sum():
    x = hit.get_value_compl()
    y = hit.get_value_compl()
    return (f'{x} + {y} = {x + y}')

def sub():
    x = hit.get_value_compl()
    y = hit.get_value_compl()
    return (f'{x} - {y} = {x - y}')
def sq():
    x = hit.get_value_compl()
    return x, math.sqrt(x)

def mult():
    x = hit.get_value_compl()
    y = hit.get_value_compl()
    return (f'{x} * {y} = {x * y}')

def expo():
    x = hit.get_value_compl()
    y = hit.get_value()
    return (f'{x} ** {y} = {x ** y}')

def div():
    count = 0
    x = hit.get_value_compl()
    y = hit.get_value_compl()
    while count == 0:
        if y == 0:
            print('На ноль делить нельзя')
            y = hit.get_value_compl()
        else:
            count = 1
            return (f'{x} / {y} = {x / y}')