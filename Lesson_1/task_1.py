while True:
    user_week = int(input("Введите порядковый номер дня недели от 1 до 7: "))
    if 1 <= user_week <= 7:
        break

days_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье" ]

if 6 <= user_week <= 7:
    print(f"{days_week[user_week - 1]}, выходной.")
else: print(f"{days_week[user_week - 1]}, рабочий день.")