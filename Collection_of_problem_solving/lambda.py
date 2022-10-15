#

# def sum(x, y):
#     return x+y

def calc(op, a, b):
    print(op(a, b))

# sum = lambda x, y: x+y

calc(lambda x, y: x+y, 4, 5) # пропускает этапы присваивания функции переменной.
