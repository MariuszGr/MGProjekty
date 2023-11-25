#Zad1
# w = int(input("podaj wiek: "))
# if w < 4:
#     print("cena biletu: 0zł")
# elif (w >= 4) and (w <= 18):
#     print("cena biletu: 10zł")
# elif w > 18:
#     print("cena biletu: 20zł")

#zad2
# L = input("podaj litere: ")
#
# if L.islower():
#     print("litera jest mala")
# elif not L.islower():
#     print("litera jest duza")

#zad3
# print("jaką operacje chcesz wykonac?")
# print("1) dodawanie")
# print("2) odejmowanie")
# print("3) mnozenie")
# print("4) dzielenie")
# print("5) potegowanie")
# opcja = int(input("wypisz numer operacji: "))
# x = int(input("podaj argument 1: "))
# y = int(input("podaj argument 2: "))
# if opcja == 1:
#     print(f"wynik: {x + y}")
# elif opcja == 2:
#     print(f"wynik: {x - y}")
# elif opcja == 3:
#     print(f"wynik: {x * y}")
# elif opcja == 4:
#     print(f"wynik: {x / y}")
# elif opcja == 5:
#     print(f"wynik: {x ** y}")

#zad4
# import math
# a = int(input("podaj  a: "))
# b = int(input("podaj  b: "))
# c = int(input("podaj  c: "))
# d = b**2 - 4*a*c
# if d > 0:
#     p_d = math.sqrt(d)
#     print(f"delta: {d}")
#     print(f"pierwaistek z delty: {p_d}")
#     x1 = (-b - p_d) / float(2*a)
#     x2 = (-b + p_d) / float(2*a)
#     print(f"rozwiazania: x1: {x1} lub x2: {x2}")
# elif d == 0:
#     print(f"ddelta: {d}")
#     x = -b / float(2*a)
#     print(f"rozwiązanie x: {x}")
# elif d < 0:
#     print(f"ddelta: {d}")
#     print("rownanie nie ma rozwiazan")

#zad5
# x = int(input("podaj x: "))
# y = int(input("podaj y: "))
# z = int(input("podaj z: "))
# print(f"podane liczby {x, y, z}")
# if x > y:
#     x, y = y, x
# if y > z:
#     y, z = z, y
# if x > y:
#     x, y = y, x
# print(f"uporzadkowane od najmniejszej do najwiekszej {x, y, z}")

#Zadania dodatkowe
#Zad1

#a
# x = int(input("podaj x: "))
# if x > 0:
#     a = 2 * x
# elif x == 0:
#     a = 0
# elif x < 0:
#     a = -3 * x
# print(f"wartosc funkcji wynsoi: {a}")

#b
# x = int(input("podaj x: "))
# if x >= 1:
#   b = x**2
# elif x < 1:
#   b = x
# print(f"wartosc funkcji wynsoi: {b}")

#c
# x = int(input("podaj x: "))
# if x > 2:
#   c = 2 + x
# elif x == 2:
#   c = 8
# elif x < 2:
#   c = x - 4
# print(f"wartosc funkcji wynsoi: {c}")

#Zad2
# print("pada deszcz? ")
# p = bool(int(input("jesli tak wpisz 1, jesli nie wpisz 0: ")))
# print("autobus jest na przystanku? ")
# q = bool(int(input("jesli tak wpisz 1, jesli nie wpisz 0: ")))
# if p and q:
#   print("wez parasol, dostaniesz sie na uczelnie")
# elif p and not q:
#   print("nie dostaniesz sie na uczelnie")
# elif not p and q:
#   print("dostaniesz się na uczelnie, miłego dnia i pieknej pogody")

#Zad3
# def changing_letter(l):
#   if l.islower():
#       l = l.upper()
#   elif not l.islower():
#       l = l.lower()
#   return  l
# l = input("podaj litere: ")
# z = changing_letter(l)
# print(f"zmieniona litera: {z}")