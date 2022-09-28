x = int(input("Введите x: "))
y = int(input("Введите y: "))

if x > 0 and y > 0:
    print(f"({x};{y}) принадлежит ПЕРВОЙ четверти")
elif x < 0 and y > 0:
    print(f"({x};{y}) принадлежит ВТОРОЙ четверти")
elif x < 0 and y < 0:
    print(f"({x};{y}) принадлежит ТРЕТЬЕЙ четверти")
elif x > 0 and y < 0:
    print(f"({x};{y}) принадлежит ЧЕТВЕРТОЙ четверти")
elif x == 0 or y == 0:
    print(f"({x};{y}) точка находится на оси")