# NO 7
# n = int (input("n = "))
# s = 0
# for i in range(1, n + 1):
#   if i % 2 == 1:

# NO 11
# n = int(input('n ='))
# _max = None
# _min = None

# i = 0
# while i < n:
#     a = int(input('a = '))
#     i += 1
#     if i % 2 == 0:
#         if _max == None or _max < a:
#             _max = a
#     else:
#         if _min is None or _min > a:
#             _min = a
# print(_max, _min)


# max qiymatini topish N028
# n = int(input('n ='))
# _max = None
# i = 0
# while i < n:
#   a = int(input('a = '))
#   i += 1
#   if _max == None or _max < a:
#     _max = a
# print(_max)

# NO28
# close = 0
# close_index = None
# money = int(input('money= '))
# i = 0
# while i < 10:
#     i += 1
#     home_price = int(input('home price '))

#     if close_index == None or close > abs(home_price - money):
#         close = abs(home_price - money)
#         close_index = i
# print(close_index)


# Dars 6

# n ikkining nechinchi darajasini topish
# def sum(n):
#     if n > 0:
#         s = n // 2
#     return s


# a = int(input('a = '))
# n = sum(a)
# print(n)


# def sum_abs(a, b, c):
#     n = a + b + c
#     return n


# t = int(input('t = '))
# t1 = int(input('t1 = '))
# t2 = int(input('t2 = '))
# n = sum_abs(t, t1, t2)
# print(n)


# uy ishi
# NO 1
# a = float(input("a = "))
# print(a)


# NO 2
# a = int(input("a = "))
# print(a)

# NO 3
# a = str(input("a = "))
# print(a)

# NO 4
# a = int(input('a = '))
# b = abs(a)
# print(b)

# NO 5
# a = str(input("a = "))
# a = ascii(a)
# print(a)

# NO 6
# a = int(input("a = "))
# a = bin(a)
# print(a)

# NO 7
# a = int(input("a = "))
# a = oct(a)
# print(a)

# NO 8
# def sum_abs(a, b, c):
#     n = a + b + c
#     return n


# t = int(input('t = '))
# t1 = int(input('t1 = '))
# t2 = int(input('t2 = '))
# n = sum_abs(t, t1, t2)
# print(n)

# NO 9
# a = int(input("a = "))
# b = int(input("b = "))
# a = pow(a, b)
# print(a)

# NO 10
# for i in range(0, 10, 2):
#   print(i)

# NO 13


# NO 15
# a = int(input("a = "))
# b = id(a)
# print(b)

# NO 16
# a = int(input('a = '))
# b = bytearray(a)
# print(b)

# NO 17
# a = int(input('a = '))
# b = bytes(a)
# print(b)

# NO 18
# a = int(input('a = '))
# b = callable(a)
# print(b)

# NO 19
# a = int(input('a = '))
# b = chr(a)
# print(b)

# NO 20
# a = int(input("a = "))
# b = int(input("b = "))
# c = a + b
# print("a={0} + b={1} = c={2}".format(a, b, c))

# NO 21
# n = int(input("Nechta son kiritmoqchisiz? >_"))
# max_n = None
# min_n = None
# for i in range(n):
#     a = int(input())
#     if i == 0:
#         max_n = a
#         min_n = a
#     else:
#         if max_n < a:
#             max_n = a
#         elif min_n > a:
#             min_n = a
# print(f"Eng kattasi = {max_n}\nEng kichigi = {min_n}")

# NO 22
# globals()

# NO 23
# locals()


# NO 24
# help()


# No 4.2/1
# def sender(s):
#     result = ""
#     i = 0
#     while i < len(s):
#         result += str(ord(s[i])) + ";"
#         i += 1
#     return result


# def receiver(s):
#     result = ""
#     for item in s.split(';'):
#         if item != "":
#             result += chr(int(item))
#     return result


# s = input('s = ')
# coding = sender(s)
# print(coding)
# coding_1 = receiver(coding)
# print(coding_1)

# NO 2

# import math


# def toBinary(a):
#     l, m = [], []
#     for i in a:
#         l.append(ord(i))
#     for i in l:
#         m.append(int(bin(i)[2:]))
#     return m


# def toString(a):
#     l = []
#     m = ""
#     for i in a:
#         b = 0
#         c = 0
#         k = int(math.log10(i))+1
#         for j in range(k):

#             b = ((i % 10)*(2**j))
#             i = i//10
#             c = c+b
#             l.append(c)
#     for x in l:
#         m = m+chr(x)
#     return m


# s = "nima gap sezr aka"
# kodcha = toBinary(s)
# print(kodcha)

# kodcha1 = toString(kodcha)
# print(kodcha1)


# NO 3
