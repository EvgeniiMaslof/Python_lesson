# with open('file.txt', 'a') as data:   # Способ записи данных в файл с автоматическим закрытием файла
#     data.write('line 1986\n')
#     data.write('line 2022\n')
#
# exit()
#
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # путь к файлу который открываем
# data.writelines(colors)      # передаем данные для записи в файл
# data.write('\nLINE2\n')
# data.write('LINE3\n')
# data.close()                 # закрываем файл для дальнейшей работы

# exit()  # позволяет не выполнять код написанный дальше
path = 'file.txt'   # чтение данных из файла
data = open(path, 'r')
for line in data:
    print(line)
data.close()


