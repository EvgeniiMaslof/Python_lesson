# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

# Пользовательский ввод
text_user = input('Введите ваш текс на русском языке: ').split()

result = ' '.join([text_user[i] for i in range(len(text_user)) if 'абв' not in text_user[i]])
print(result)