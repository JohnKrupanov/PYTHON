# Lesson 1

# Task 1
# Найдите сумму цифр трехзначного числа n.
# Результат сохраните в перменную res.

# n = 783
# n1 = n // 100 # Нахождение первой цифры числа
# n2 = (n % 100) // 10 # Нахождение второй цифры числа
# n3 = n % 10 # Нахождение третьей цифры числа
# res = n1 + n2 + n3
# print(res)

# Task 2 
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Выведите через пробел количество журавликов, сделанных Петей, Катей и Сережей.

# # n = 60
# a = int(n/6)
# b = int(n/6*4)
# c = int(n/6)

# print(a, b, c)

# Task 3
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

# n = 123456

# number_1 = n // 1000
# number_2 = n % 1000

# n1 = number_1 // 100 # Нахождение первой цифры числа
# n2 = (number_1 % 100) // 10 # Нахождение второй цифры числа
# n3 = number_1 % 10 # Нахождение третьей цифры числа
# l = int(n1) + int(n2) + int(n3)

# m1 = number_2 // 100 # Нахождение первой цифры числа
# m2 = (number_2 % 100) // 10 # Нахождение второй цифры числа
# m3 = number_2 % 10 # Нахождение третьей цифры числа
# r = int(m1) + int(m2) + int(m3)

# if l == r:
#     print('yes')
# else:
#     print('no')

# Task 4
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

# a = 3
# b = 2
# c = 1

# if c%a == 0 or c%b == 0:
#     print('yes')
# else: print('no')

# Lesson 2
# Task1.
# coins = [0, 1, 0, 1, 1, 0]
# count_zero = 0
# count_one = 0

# for coin in coins:
#     if coin == 0:
#         count_zero += 1
#     else:
#         count_one += 1

# if count_one > count_zero:
#     print(count_zero)
# else:
#     print(count_one)

# Task2.
# s = int(input('Введите сумму числе: '))
# p = int(input('Введите произведение: '))
# a = 0
# for i in range(s):
#     for j in range(p):
#         if s == i + j and p == i * j:
#             print(i, j)

# Task3.
# n = int(input('Введите число N: '))
# k = 0
# res = 1
# while res < n+1:
#     print(res, end=' ')
#     k += 1
#     res = 2 ** k


# Task3.
# n = int(input())
# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1

# Lesson 3
# Task 16
# list_1 = [1, 2, 3, 4, 5, 3, 3] 
# k = 3 
# count_k = 0 
# for i in list_1: 
#         if i == k: 
#             count_k += 1 
# print(count_k)

from csv import list_dialects


# Task 18
# List_1 = [1, 2, 3, 4, 5, 16]
# k = 10

# def nearval(List_1, number):
#     return min(List_1, key=lambda k: abs(number - abs(k))) 
# print(nearval(List_1, k))

# Task 20

# k = "Lizard"

# import re
# def Scrabble(text):
#     return bool(re.search("[а-яА-Я]", text))
# Rus = { 1:"А, В, Е, И, Н, О, Р, С, Т", 2:"Д, К, Л, М, П, У", 3:"Б, Г, Ё, Ь, Я", 4:"Й, Ы", 5:"Ж, З, Х, Ц, Ч", 8:"Ш, Э, Ю", 10:"Ф, Щ, Ъ"}
# Eng = { 1:"A, E, I, O, U, L, N, S, T, R ", 2:"D, G", 3:"B, C, M, P", 4:"F, H, V, W, Y", 5:"K", 8:"J, X", 10:"Q, Z"}
# text = (k).upper()
# if Scrabble(text):
#      print(sum([k for i in text for k, v in Rus.items() if i in v]))
# else: print(sum([k for i in text for k, v in Eng.items() if i in v]))