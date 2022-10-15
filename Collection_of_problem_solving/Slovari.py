dictionari = {} # пустой словарь # использование ключей в словарях \ - для написания сразных строк
dictionari = \
    {
      'up': 'v',
      'left': 'l',
      'down': 'd',
      'right': 'r'
    }
print(dictionari)
print(dictionari['left'])

for k in dictionari.keys(): # keys просмотр ключей в словаре
    print(k)
for k in dictionari.values():  # keys просмотр значений в словаре
    print(k)
    for item in dictionari:  # keys просмотр значений в словаре
        print('{}: {}'.format(item, dictionari[item])) # одновременный просмотр и ключей и значений
