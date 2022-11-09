# a = 65
# shifr_a = bin(a)
# print(shifr_a)
# deshifr = int(shifr_a, 2)
# print(deshifr)


# NO 4.2/3
# def sender(text, key):
#     i = 0
#     result = ""
#     while i < len(text):
#         result += chr(ord(text[i]) ^ key)
#         i += 1
#     return result


# def receiver(text, key):
#     i = 0
#     result = ""
#     while i < len(text):
#         result += chr(ord(text[i]) ^ key)
#         i += 1
#     return result


# coding = input('text = ')
# key = 10
# coding1 = sender(coding, key)
# print(coding1)
# coding1 = sender(coding1, key)
# print(coding1)


# Dars
# a = " Dasturchining quroli bu Internet "
# print(a[24:])

# a = "Dasturchining quroli bu Internet"
# print(a[::-1])

# a = 'A'
# b = a * 10
# print(b)


# name = "Tom"
# age = 23

# templed = f"His/her name is {name}, he/she is {age} years old"
# print(templed)

# s = 'Salom olam'
# s = s.upper()
# print(s)
# print(s[0:2].lower())

# probel olib tashlaydi
# s = "  salom"
# print(s.strip())


# sonlarni oladi true
# phone_number = "23877421"
# print(phone_number.isdigit())

# 1-usul
# a = "salom dunyo"
# b = "dunyo"
# c = a.endswith(b)
# print(c)

# 2-usul
# a = "salom dunyo"
# b = "dunyo"
# c = a.find(b)
# print(c)

# 3-usul

# UY ishi
# NO 1
# def sum(a, b):
#     c = a + b
#     return c


# a = int(input('a = '))
# b = int(input('b = '))
# n = sum(a, b)
# print(n)


# NO 2
# def max(a, b):
#     if a > b:
#         return a
#     else:
#         return b


# def min(a, b):
#     if a < b:
#         return a
#     else:
#         return b


# a = int(input('a = '))
# b = int(input('b = '))
# max = max(a, b)
# min = min(a, b)
# print("Max", max)
# print("Min", min)

# NO 3
# def max(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c


# def min(a, b, c):
#     if a < b and a < c:
#         return a
#     elif b < a and b < c:
#         return b
#     else:
#         return c


# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))
# max = max(a, b, c)
# min = min(a, b, c)
# print("Max", max)
# print("Min", min)

# NO 4
# def sum(a):
#     if a > 0:
#         return a
#     else:
#         c = (a - a) - a
#         return c


# a = int(input('a = '))
# sum = sum(a)
# print("Natija: ", sum)


# NO 5
# def IsEven(a):
#     c = a % 2 == 0
#     return c


# a = int(input("a = "))
# IsEven = IsEven(a)
# print("Natija: ", IsEven)


# NO 6
# def IsOdd(a):
#     c = a % 2 == 1
#     return c


# a = int(input("a = "))
# IsOdd = IsOdd(a)
# print("Natija: ", IsOdd)

# NO 7
# def ConvertMoney(a):
#     c = a / 10000
#     return c


# a = int(input("So'm = "))
# n = ConvertMoney(a)
# print("Dollar: ", n)

# NO 8
# def sum(a, b):
#     if a > b:
#         return True
#     else:
#         return False


# a = int(input("Mablag': "))
# b = int(input("Tovar narxi: "))
# sum = sum(a, b)
# print("Natija: ", sum)

# Uyga vazifa (01.02.2022): 4.2. dan 4,5 va 5.1


# NO 9
# def sum(rahbar):
#     if rahbar > 8 and rahbar < 17:
#         return True
#     else:
#         return False


# rahbar = int(input("Rahbar ishchisiga topshiriq bermoqchi bo'lgan vaqt: "))
# sum = sum(rahbar)
# print("Natija: ", sum)

# NO 10
# def sum(n):
#     sum_n = n * 2.4
#     return sum_n


# n = int(input("Kg: "))
# sum = sum(n)
# print(sum)


# NO 12


# NO 13
# def string(n):
#     text1 = "The most "
#     text2 = "brilliant "
#     text3 = "exciting "
#     text4 = "fantastic virtuous heart-warming tear-jerking beautiful exhilarating emotional inspiring "
#     if n // 1 == 0:
#         c = text1 + text2 + str(n)
#     elif n // 2 == 0:
#         c = text1 + text3 + str(n)
#     elif n / 3 == 0:
#         c = text1 + text4 + str(n)
#     else:
#       c = 0
#     return c


# n = int(input("n = "))
# string1 = string(n)
# print(string1)

# NO 14
# def asr(a):
#     b = a // 100
#     return b


# a = int(input("yil kiriting\n>>> "))
# b = asr(a)
# print(f"{a} yil {b} asrga teng")

# NO 12
# def IsPolindrom(Num):
#     Temp = Num
#     rev = 0
#     while(Num > 0):
#         dig = Num % 10
#         rev = rev * 10 + dig
#         Num = Num // 10
#     if(Temp == rev):
#         return True
#     else:
#         return False


# Num = int(input("Enter a value:"))
# polindrom = IsPolindrom(Num)
# print("Natija: ", polindrom)


# NO 11
# def online(n):
#     a = """no one online"""
#     b = "user1 online"
#     c = "user1 va user2 online"
#     if n == 0:
#         return a
#     elif n == 1:
#         return b
#     elif n == 2:
#         return c
#     elif n > 2:
#         f = "user -2"
#         l = f"{b} + {c} + {f}"
#         return l


# n = int(input("n ="))
# online_1 = online(n)
# print(online_1)
