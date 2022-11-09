

#a = ascii('$')
# print(a)


# ikkilik sanoq sistemasiga o'tqazadi
# bin(10)


# baytga o'tqizadi
# a = bytearray(40)
# print(a)


# sonni harfga o'tkazadi
# a = chr(2)
# print(a)


# stringda yozilgan kodni ishlatadi
#exec(compile('a=5\nb=7\nprint(a+b)', '', 'exec'))

# hamma yozilgan kodni chiqaradi
# globals()

# kodlab beradi
# a = 'orange'
# hash(a)

# NO 1
# n marta chiqarish
# n = int(input("n = "))
# a = "Salom olam"
# while n > 0:
#     print(a)
#     n -= 1

# NO 2
# n = int(input("n = "))
# a = 0
# while n > 0:
#     print(a)
#     a += 1
#     n -= 1


# No 3
# n = int(input("n = "))
# a = 0
# b = 1

# if n % 2 == 0:
#     while n > 0:
#         print(a)
#         n -= 1
# else:
#     while n > 0:
#         print(b)
#         n -= 1


# NO 4
# n = int(input("n = "))
# a = 0
# while n >= a:
#     print(a)
#     a += 2


# NO 5
# n = int(input("n = "))
# a = 1
# while n >= a:
#     print(a)
#     a += 2


# NO 6
# n = int(input("n sonini kiriting: "))
# s = 0
# i = 0
# while i < n:
#     s = s+i
#     i += 1
# print(s)


# NO 7
# n = int(input("n sonini kiriting: "))
# s = 0
# i = 1
# while i < n:
#     s = s+i
#     i += 2
# print(s)


# NO 8
# n = int(input("n sonini kiriting: "))
# s = 0
# i = 0
# while i < n:
#     s = s+i
#     i += 2
# print(s)


# NO 9
# n = 15
# a = 0
# while n > a:
#     print(bin(a))
#     a += 1

# NO 10
# n = int(input("kiritiladigan raqamlar soni = "))
# a = 0
# while n > 0:
#     b = int(input("a = "))
#     if (b != 0) & (b > 0):
#         a += b
#     elif b > 0:
#         a += b
#     n -= 1
# print("natija", a)

# NO 11 tashab ketildi

# No 13
# n = int(input("kiritiladigan raqamlar soni = "))

# while n > 0:
#     a = int(input("a ="))
#     if a % 2 == 0:
#         print("natija", a)
#     else:
#         a = 0
#     n -= 1

# No 17
# n = int(input("kiritiladigan raqamlar soni = "))
# b = 0
# while n > 0:
#     a = int(input("a ="))
#     if a > 0:
#         b += 1
#     n -= 1
# print("Musbat sonlar:", b)


# No 18
# n = int(input("kiritiladigan raqamlar soni = "))
# b = 0
# while n > 0:
#     a = int(input("a ="))
#     if a < 0:
#         b += 1
#     n -= 1
# print("Manfiy sonlar:", b)

# No 19
# n = int(input("kiritiladigan raqamlar soni = "))
# b = 0
# while n > 0:
#     a = int(input("a ="))
#     if a < 0:
#         b += 1
#     n -= 1
# print("Musbat sonlar:", b)

# NO 23
# n = int(input("kiritiladigan raqamlar soni = "))
# b = 0
# t = 0
# while n >= 0:
#     a = int(input("a = "))
#     while a > 0:
#         b += 1
# n -= 1
# print("Natija: musbatlari ", b)
# print("Natija: toqlari ", t)

# NO 30
# n = int(input("Nechta son kiritmoqchisiz? >_"))
# max_n = 0
# min_n = 0
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
