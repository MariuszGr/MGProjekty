#zad 3
# bok1=float(input("podaj dlugosc pierwszego boku:"))
# bok2=float(input("podaj dlugosc drugiego boku: "))
# p=bok1*bok2
# o=(2*bok1)+(2*bok2)
# print(f"pole wynosi {p:.2f}, a obwod {o:.2f}")

#zad 4
# d=float(input("przebyta droga: "))
# sp=float(input("srednie spalanie: "))
# zp=d*sp/100
# k=zp*6.5
# print(f"przewidywane zuzycie paliwa wynosi {zp:.2f} litrow, koszty szacowane na {k:.2f} zlotych")

#zad 4.1
# import random
# d=random.randint(1,100000)
# sp=float(input("srednie spalanie: "))
# zp=d*sp/100
# k=zp*6.5
# print(f"przewidywane zuzycie paliwa na trasie o dlugosci {d:.2f} kilometrow wynosi {zp} litrow, koszty szacowane na {k:.2f} zlotych")

#zadania dodatkowe

#1
# x > 0 => a(x) = 2x
# x = 0 => a(x) = 0
# x < 0 => a(x) = -3x
# x podaje użytkownik, y-wartość funkcji dla podanego x
# x = int(input("Podaj liczbę: "))
# #
# if x > 0:
# y = 2 * x
# elif x == 0:
# y = 0
# elif x < 0:
# y = -3 * x
# #
# print(f"Wartość funkcji dla podanego x wynsoi: {y}")

#2
# import math
# a=float(input("podaj dlugosc boku a:"))
# b=float(input("podaj dlugosc boku b:"))
# c=float(input("podaj dlugosc boku c:"))
# p=(a+b+c)/2
# pole=math.sqrt(p*(p-a)*(p-b)*(p-c))
# print(f"pole (w zaokragleniu) wynosi {pole:.2f}")

#3
# a=float(input("podaj pierwsza liczbe:"))
# b=float(input("podaj druga liczbe:"))
# suma=a+b
# roznica=a-b
# iloczyn=a*b
# iloraz=a/b
# print(f"suma liczb wynosi {suma}, roznica {roznica}, iloczyn {iloczyn}, iloraz {iloraz}")