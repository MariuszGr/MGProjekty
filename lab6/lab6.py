import random

# #Zad 1
# #a)
#
# lucky_number = random.randint(1,11)
# print(lucky_number)
#
# #b)
#
# roczniki = [1994, 1998, 2001, 2002, 2003, 2004]
# lucky_year = random.randint(0, len(roczniki) - 1)
# print(roczniki[lucky_year])
#
# #c)
#
# lotek = []
# for i in range(1, 50):
#     lotek.append(i)
#
# print(lotek)
# kule = random.sample(lotek, 6)
# print(kule)

#Zad 2

import math
# #a)
# a = math.sqrt(81)
# print(a)
#
# #B)
# b = math.pow(8, 10)
# print(b)
#
# #c)
#
# c = math.sqrt(2)
# d = math.sqrt(3)
# e = math.sqrt(6)
#
# suma = c + d + e
# suma = round(suma, 2)
# print(suma)
#
# #d)
#
# # f = math.sqrt(-5)
# # print(f)
#
# #e)
#
# g = math.pow(125, 1.0/3)
# print(g)

#Zad 3

# import time
#
# czas = int(input("Podaj czas jaki ma być odliczany: "))
#
# while czas > 0:
#     print(czas)
#     time.sleep(1)
#     czas -= 1
#
# print("Koniec odliczania")

#Zad 4
# from _datetime import datetime
#
# data_zajec = "2023-12-10"
# format = "%Y-%m-%d"
#
# data = datetime.strptime(data_zajec, format)
# print(data)
# actual_date = datetime.now()
#
# roznica_czasu = actual_date - data
# print(roznica_czasu)
#
# data_kolokwium = "2024-02-10"
# data1 = datetime.strptime(data_kolokwium, format)
# print(data1)
# roznica_czasu_2 = data1 - actual_date
# print(roznica_czasu_2)

#Zad 5
# import keyword
#
# list1 = ['for', 'print', 'break', 'done', 'bad']
#
# for i in range(0, len(list1)):
#     print(keyword.iskeyword(list1[i]))

#zad 7
# import random
# import math
#
# def geometric_mean(numbers):
#     product = 1
#     for num in numbers:
#         product *= num
#     return math.pow(product, 1/len(numbers))
#
# def main():
#     lower_limit = float(input("Podaj dolny przedział losowania: "))
#     upper_limit = float(input("Podaj górny przedział losowania: "))
#     random_numbers = [random.uniform(lower_limit, upper_limit) for _ in range(10)]
#     print(f"Wylosowane liczby: {random_numbers}")
#     mean_geo = geometric_mean(random_numbers)
#     print(f"Średnia geometryczna: {mean_geo}")
#
# if __name__ == "__main__":
#     main()

