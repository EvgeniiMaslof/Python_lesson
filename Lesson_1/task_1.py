numbers_week = int(input("Введите номер дня недели от 1 до 7: "))
days_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
if 1 <= numbers_week <= 5:
    print(f"{days_week[numbers_week - 1]}, рабочий день.")
elif 6 <= numbers_week <= 7:
    print(f"{days_week[numbers_week - 1]}, выходной.")
else:
    print("Неправилное число, попробуйте снова.")