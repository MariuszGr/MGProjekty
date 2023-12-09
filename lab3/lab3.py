#zad1
# a=(int(input("Podaj pierwsza liczbe: ")))
# b=(int(input("Podaj druga liczbe: ")))
# w=a
# m=b
# if b>a:
#     w=b
#     m=a
# while m<=w:
#     print(m)
#     m=m+1

#zad2
# x=-4
# y=2*x*x-(5*x)-8
# while x<=4:
#     print(f"y=2𝑥2−5𝑥−8, dla x rownego {x} wynosi {y}")
#     x=x+0.5
#     y = 2 * x * x - (5 * x) - 8

#zad3
# a=(int(input("Podaj liczbe: ")))
# while a>=0:
#     a = (int(input("Podaj liczbe: ")))

#zad4
# a=(int(input("Podaj pierwsza liczbe: ")))
# b=int(input("Podaj druga liczbe: "))
# w=a
# m=b
# if b>a:
#      w=b
#      m=a
# m=m-1
# while m<w:
#     m = m + 1
#     if m % 2 > 0:
#         continue
#     print(m)

#zadania dodatkowe

#zad1
# n=(int(input("Podaj liczbe studentow: ")))
# a=1
# b=0
# while a<=n:
#     p=(int(input(f"Podaj liczbe punktow studenta nr {a}: ")))
#     b=b+p
#     a=a+1
# s=b/n
# print(f"srednia ilosc punktow na studenta wynosi {s}")

#zad2
# a=1
# b=0
# n=0
# while True:
#     p=(int(input(f"Podaj liczbe punktow studenta nr {a}: ")))
#     if p>100:
#         break
#     b=b+p
#     a=a+1
#     n=n+1
# s=b/n
# print(f"srednia ilosc punktow na studenta wynosi {s}")

################################################################
#zad1
# for i in range(1, 101):
#     print(i)

# for i in range(100, 0-1, -1):
#     print(i)

# for i in range(7, 78, +7):
#     print(i)

# for i in range(20,-1, -2):
#     print(i)

#zad2
# n=(int(input("Podaj liczbe wierszy: ")))
# for i in range(n):
#     print("***")

#zad3
# n=(int(input("Podaj wysokosc choinki: ")))
# w="*"
# for i in range(n):
#     print(w)
#     w=w+"*"

#zad4
# n=int(input("podaj n:"))
# a=int(input("podaj a:"))
# r=int(input("podaj r:"))
# print(a)
# for i in range (n-1):
#     a=a+r
#     print(a)

#zad5
# n=int(input("Podaj liczbe: "))
# s=1
# a=1
# for i in range (n):
#     s=s*a
#     a=a+1
# print(s)

#zadania dodatkowe

#zad1   

#############################################
#zad1
# tekst = "Rzeszów jest piękny"
# print(tekst[0])
# print(tekst[6: 12: 3], tekst[1])

#zad2
# tekst ="Python jest super"
# print(tekst[0])
# a=len(tekst)-1
# print(tekst[a])
# print(tekst[0: a+1: 2])
# print(tekst[1: a+1: 3])
# print(tekst[10: a+1])
# print(tekst[a+1: 0: -1])