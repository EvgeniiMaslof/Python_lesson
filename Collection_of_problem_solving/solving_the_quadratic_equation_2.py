from math import sqrt


def roots_equ(a, b, c):
    d = b ** 2 - 4 * a * c
    with open("roots.txt", "a", encoding="utf-8") as my_f:
        my_f.write(f"{a}x ** 2 + {b}x + {c}\n")
        if d > 0 and a:
            my_f.write(f"The first root: {(-b + sqrt(d)) / (2 * a):.2f}\n")
            my_f.write(f"The first root: {(-b - sqrt(d)) / (2 * a):.2f}\n")
        elif d == 0 and a:
            my_f.write(f"The root: {-b / (2 * a):.2f}\n")
        else:
            my_f.write("There are no roots.\n")
print("Введите коэффициенты квадратного уравнения")
a = float(input("а = "))
b = float(input("b = "))
c = float(input("c = "))
roots_equ(a, b, c)