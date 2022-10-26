import math
import here_is_the_data as hit

x = 0
y = 0

def init(a, b):
    global x
    global y
    x = a
    y = b

def sum():
    x = hit.get_value()
    y = hit.get_value()
    return (f'{x} + {y} = {x + y}')

def sub():
    x = hit.get_value()
    y = hit.get_value()
    return (f'{x} - {y} = {x - y}')

def sq():
    x = hit.get_value()
    return (f'{x} = {math.sqrt(x)}')

def mult():
    x = hit.get_value()
    y = hit.get_value()
    return (f'{x} * {y} = {x * y}')

def expo():
    x = hit.get_value()
    y = hit.get_value()
    return (f'{x} ** {y} = {x ** y}')

def div():
    x = hit.get_value()
    y = hit.get_value()
    return (f'{x} / {y} = {x / y}')
