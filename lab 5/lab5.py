#1
# import math
#
# def pole_kola():
#     try:
#         promien = float(input("Podaj promień koła: "))
#         pole = math.pi * promien**2
#         print(f"Pole koła o podanym promieniu wynosi {pole:.2f}.")
#
#     except ValueError:
#         print("Błąd: Podana wartość nie jest liczbą.")
# pole_kola()

#2
# def pole_trapezu():
#     try:
#         a = float(input("Podaj długość pierwszej podstawy (a): "))
#         b = float(input("Podaj długość drugiej podstawy (b): "))
#         h = float(input("Podaj wysokość trapezu (h): "))
#
#         if a <= 0 or b <= 0 or h <= 0:
#             print("Błąd: Wartości muszą być dodatnie.")
#             return None
#
#         pole = 0.5 * (a + b) * h
#         return pole
#
#     except ValueError:
#         print("Błąd: Podane wartości nie są liczbami.")
#         return None
#
# wynik = pole_trapezu()
#
# if wynik is not None:
#     print(f"Pole trapezu o podanych wymiarach wynosi {wynik:.2f}.")

#3
# def wypisz_imie_i_wiek(imie, wiek=20):
#     """
#     Funkcja wypisująca imię i wiek na ekranie.
#
#     Parametry:
#     - imie: Imię do wypisania.
#     - wiek: Wiek do wpisania
#     """
#     print(f"Imię: {imie}, Wiek: {wiek}")
#
#
# wypisz_imie_i_wiek("Jan")
#
# print(wypisz_imie_i_wiek.__doc__)

#4
# def sprawdz_dodatniosc():
#     """
#     Funkcja sprawdzająca, czy podana liczba jest dodatnia.
#     """
#     try:
#         x = float(input("Podaj liczbę x: "))
#
#         if x > 0:
#             print(f"Liczba {x} jest dodatnia.")
#         elif x == 0:
#             print("Liczba wynosi 0.")
#         else:
#             print(f"Liczba {x} nie jest dodatnia.")
#
#     except ValueError:
#         print("Błąd: Podana wartość nie jest liczbą.")
#
# sprawdz_dodatniosc()

#5
# def oblicz_bmi(waga, wzrost_cm):
#     """
#     Funkcja obliczająca wskaźnik BMI na podstawie wagi i wzrostu.
#
#     Parametry:
#     - waga: Waga w kilogramach.
#     - wzrost_cm: Wzrost w centymetrach.
#
#     Wynik:
#     - Wskaźnik BMI lub None, jeśli waga lub wzrost są niepoprawne.
#     """
#     if waga <= 0 or wzrost_cm <= 0:
#         return None
#
#     wzrost_m = wzrost_cm / 100  # Konwersja wzrostu z cm na m
#     bmi = waga / (wzrost_m ** 2)
#     return bmi
#
# def interpretuj_bmi(bmi):
#     """
#     Funkcja interpretująca wskaźnik BMI i informująca użytkownika o zakresie.
#
#     Parametry:
#     - bmi: Wskaźnik BMI lub None, jeśli waga lub wzrost są niepoprawne.
#     """
#     if bmi is None:
#         print("Błąd: Waga i wzrost muszą być dodatnie.")
#     elif bmi < 18.5:
#         print(f"Twój BMI wynosi {bmi:.2f} - niedowaga.")
#     elif 18.5 <= bmi < 24.9:
#         print(f"Twój BMI wynosi {bmi:.2f} - prawidłowa waga.")
#     elif 25 <= bmi < 29.9:
#         print(f"Twój BMI wynosi {bmi:.2f} - nadwaga.")
#     else:
#         print(f"Twój BMI wynosi {bmi:.2f} - otyłość.")
#
# # Wywołanie funkcji:
# try:
#     waga = float(input("Podaj wagę (kg): "))
#     wzrost_cm = float(input("Podaj wzrost (cm): "))
#
#     bmi = oblicz_bmi(waga, wzrost_cm)
#     interpretuj_bmi(bmi)
#
# except ValueError:
#     print("Błąd: Podane wartości nie są liczbami.")

#6
# def pole_trojkata(a, b, c):
#     """
#     Funkcja obliczająca pole trójkąta na podstawie długości boków.
#
#     Parametry:
#     - a, b, c: Długości boków trójkąta.
#
#     Wynik:
#     - Pole trójkąta.
#     """
#     try:
#         # Sprawdzenie warunku trójkąta
#         if a + b > c and a + c > b and b + c > a:
#             p = (a + b + c) / 2
#             pole = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#             return pole
#         else:
#             print("Błąd: Podane boki nie tworzą trójkąta.")
#             return None
#
#     except ValueError:
#         print("Błąd: Podane wartości nie są liczbami.")
#         return None
#
# # Wywołanie funkcji:
# try:
#     a = float(input("Podaj długość boku a: "))
#     b = float(input("Podaj długość boku b: "))
#     c = float(input("Podaj długość boku c: "))
#
#     pole = pole_trojkata(a, b, c)
#
#     if pole is not None:
#         print(f"Pole trójkąta o bokach {a}, {b}, {c} wynosi {pole:.2f}.")
#
# except ValueError:
#     print("Błąd: Podane wartości nie są liczbami.")

#7
# def odwroc_string(tekst):
#     """
#     Funkcja odwracająca ciąg znaków.
#
#     Parametry:
#     - tekst: Ciąg znaków do odwrócenia.
#
#     Wynik:
#     - Odwrócony ciąg znaków.
#     """
#     return tekst[::-1]
#
# # Wywołanie funkcji:
# tekst_wejsciowy = input("Podaj tekst do odwrócenia: ")
# wynik = odwroc_string(tekst_wejsciowy)
#
# print(f"Wejściowy tekst: {tekst_wejsciowy}")
# print(f"Odwrócony tekst: {wynik}")

#8
# def potega(a, n):
#     """
#     Funkcja rekurencyjna obliczająca n-ty stopień potęgi liczby a.
#
#     Parametry:
#     - a: Podstawa potęgi.
#     - n: Wykładnik potęgi.
#
#     Wynik:
#     - Wynik potęgowania a do potęgi n.
#     """
#     if n == 0:
#         return 1
#     else:
#         return a * potega(a, n-1)
#
# # Wywołanie funkcji:
# try:
#     a = float(input("Podaj liczbę a: "))
#     n = int(input("Podaj stopień potęgi n: "))
#
#     wynik = potega(a, n)
#     print(f"{a} do potęgi {n} wynosi: {wynik}")
#
# except ValueError:
#     print("Błąd: Podane wartości nie są liczbami.")

#9
# def fibonacci(n):
#     """
#     Funkcja rekurencyjna obliczająca n-ty wyraz ciągu Fibonacciego.
#
#     Parametry:
#     - n: Numer wyrazu ciągu.
#
#     Wynik:
#     - n-ty wyraz ciągu Fibonacciego.
#     """
#     if n <= 0:
#         return "Błąd: Podaj liczbę całkowitą dodatnią."
#
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# try:
#     numer = int(input("Podaj numer wyrazu ciągu Fibonacciego: "))
#
#     wynik = fibonacci(numer)
#     print(f"{numer}-ty wyraz ciągu Fibonacciego wynosi: {wynik}")
#
# except ValueError:
#     print("Błąd: Podana wartość nie jest liczbą całkowitą.")
