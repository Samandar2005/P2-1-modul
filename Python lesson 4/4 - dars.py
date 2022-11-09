# i = 1
# while i <= 100:
#     print(i)
#     i += 1
#     if i > 66:
#         break
# else:
#     print("While tugadi.")

# for i in 1, 2, 3, 4, 5, 6, 7, 8, 9, 10:
#     print(i**2)


# for i in range(10):
#     if i < 2:
#         continue

#     print(i)


# for i in range(10):
#   pass


# uy ishi


# NO 2
# x1 = int(input("x1="))
# y1 = int(input("y1="))

# x2 = int(input("x2="))
# y2 = int(input("y2="))
# if abs(x1 - x2) == 2 and abs(y1 - y2) == 1 or abs(x1 - x2) == 1 and abs(y1 - y2) == 2:
#     print("xavf soladi.")
# else:
#     print("xavf sola olmaydi")


# NO 4
# x = int(input("x = "))
# y = int(input("y = "))
# z = int(input("z = "))
# e = 0

# if (x != y & y != z):
#     n = x + y + z
#     if n < 1:
#         if x < y & x < z:
#             t = y + z / 2
#             x = t - x
#             print(x)
#         elif y < x & y < z:
#             t = x + z / 2
#             y = t - y
#             print(y)
#         else:
#             t = x + y / 2
#             z = t - z
#             print(z)
#     else:
#         if x < y:
#             t = y + z / 2
#             x = t - x
#             print(x)
#         else:
#             t = x + z / 2
#             y = t - y
#             print(y)
# else:
#     print("Xato. ")


# NO 6
# h1 = int(input("h1 = "))
# h2 = int(input("h2 = "))
# m1 = int(input("m1 = "))
# m2 = int(input("m2 = "))
# s1 = int(input("s1 = "))
# s2 = int(input("s2 = "))

# if (h1 & h2 > 0) & (h1 & h2 < 13) & (m1 & m2 >= 0) & (m1 & m2 <= 60) & (s1 & s2 > 0) & (s1 & s2 < 60):
#     if h1 > h2:
#         if m1 > m2:
#             if s1 > s2:
#                 print(f"{h1}-soat {m1}-minut {s1}-sekunt")
#         else:
#             if m1 > m2:
#                 print(f"{h1}-soat {m2}-minut {s1}-sekunt")
#             else:
#                 print(f"{h1}-soat {m2}-minut {s2}-sekunt")
#     else:
#         if m1 > m2:
#             if s1 > s2:
#                 print(f"{h2}-soat {m1}-minut {s1}-sekunt")
#         else:
#             if s1 > s2:
#                 print(f"{h2}-soat {m2}-minut {s1}-sekunt")
#             else:
#                 print(f"{h2}-soat {m2}-minut {s2}-sekunt")
# else:
#     print("Xato.")


# NO 7
# y1 = int(input("y1 = "))
# y2 = int(input("y2 = "))
# o1 = int(input("o1 = "))
# o2 = int(input("o2 = "))
# k1 = int(input("k1 = "))
# k2 = int(input("k2 = "))

# if y1 > y2:
#     if o1 > o2:
#         if k1 > k2:
#             print(f"{y1}-yil {o1}-oy {k1}-kun")
#     else:
#         if k1 > k2:
#             print(f"{y1}-yil {o2}-oy {k1}-kun")
#         else:
#             print(f"{y1}-yil {o2}-oy {k2}-kun")
# else:
#     if o1 > o2:
#         if k1 > k2:
#             print(f"{y2}-yil {o1}-oy {k1}-kun")
#     else:
#         if k1 > k2:
#             print(f"{y2}-yil {o2}-oy {k1}-kun")
#         else:
#             print(f"{y2}-yil {o2}-oy {k2}-kun")


# NO 8
# x = int(input("x = "))
# data_1 = "Dushanba"
# data_2 = "Seshanba"
# data_3 = "Chorshanba"
# data_4 = "Payshanba"
# data_5 = "Juma"
# data_6 = "Shanba"
# data_7 = "Yakshanba"

# if x == 1:
#     print(data_1)
# elif x == 2:
#     print(data_2)
# elif x == 3:
#     print(data_3)
# elif x == 4:
#     print(data_4)
# elif x == 5:
#     print(data_5)
# elif x == 6:
#     print(data_7)
# elif x == 7:
#     print(data_7)
# else:
#     print("Xatolik.")


# NO 9
# x = int(input("x = "))
# data_1 = "Yanvar"
# data_2 = "Fevral"
# data_3 = "Mart"
# data_4 = "Aprel"
# data_5 = "May"
# data_6 = "Iyun"
# data_7 = "Iyul"
# data_8 = "Avgust"
# data_9 = "Sentyabr"
# data_10 = "Oktyabn"
# data_11 = "Nayabr"
# data_12 = "Dekabr"

# if x == 1:
#     print(data_1)
# elif x == 2:
#     print(data_2)
# elif x == 3:
#     print(data_3)
# elif x == 4:
#     print(data_4)
# elif x == 5:
#     print(data_5)
# elif x == 6:
#     print(data_6)
# elif x == 7:
#     print(data_7)
# elif x == 8:
#     print(data_8)
# elif x == 9:
#     print(data_9)
# elif x == 10:
#     print(data_10)
# elif x == 11:
#     print(data_11)
# elif x == 12:
#     print(data_12)
# else:
#     print("Xato")


# NO 10
# x = int(input("x = "))
# y = int(input("y = "))

# if x > 0:
#     c = x + y
#     if c > 7:
#         r = c // 6
#         print("Xaftaning: ", r, "kuni")
#     else:
#         print("Xaftaning: ", c, "kuni")
# else:
#     print("Xatolik.")

# NO 11
# son = int(input("Son: "))
# if son > 0 and son < 10000000:
#     minglik = son//1000
#     print(minglik)
#     yuzlik = son//100 % 10
#     print(yuzlik)
#     onlik = son//10 % 10
#     print(onlik)
#     qoldiq = son % 10
#     print(qoldiq)
#     letter = ''
#     # minglik uchun
#     if minglik == 1:
#         letter += 'bir ming '
#     elif minglik == 2:
#         letter += 'ikki ming '
#     elif minglik == 3:
#         letter += 'uch ming '
#     elif minglik == 4:
#         letter += "to'rt ming "
#     elif minglik == 5:
#         letter += 'besh ming '
#     elif minglik == 6:
#         letter += 'olti ming '
#     elif minglik == 7:
#         letter += 'yetti ming '
#     elif minglik == 8:
#         letter += "sakkiz ming "
#     elif minglik == 9:
#         letter += "to'qqiz ming "
#     # yuzlik uchun
#     if yuzlik == 1:
#         letter += 'bir yuz '
#     elif yuzlik == 2:
#         letter += 'ikki yuz '
#     elif yuzlik == 3:
#         letter += 'uch yuz '
#     elif yuzlik == 4:
#         letter += "to'rt yuz "
#     elif yuzlik == 5:
#         letter += 'besh yuz '
#     elif yuzlik == 6:
#         letter += 'olti yuz '
#     elif yuzlik == 7:
#         letter += 'yetti yuz '
#     elif yuzlik == 8:
#         letter += "sakkiz yuz "
#     elif yuzlik == 9:
#         letter += "to'qqiz yuz "
#     # o'nliklar uchun
#     if onlik == 1:
#         letter += "o'n "
#     elif onlik == 2:
#         letter += 'yigirma '
#     elif onlik == 3:
#         letter += "o'ttiz "
#     elif onlik == 4:
#         letter += 'qirq '
#     elif onlik == 5:
#         letter += 'ellik '
#     elif onlik == 6:
#         letter += 'oltmish '
#     elif onlik == 7:
#         letter += "yetmish "
#     elif onlik == 8:
#         letter += 'sakson '
#     elif onlik == 9:
#         letter += "to'qson "
#     # birlik uchun
#     if qoldiq == 1:
#         letter += 'bir'
#     elif qoldiq == 2:
#         letter += 'ikki'
#     elif qoldiq == 3:
#         letter += 'uch'
#     elif qoldiq == 4:
#         letter += "to'rt"
#     elif qoldiq == 5:
#         letter += 'besh'
#     elif qoldiq == 6:
#         letter += 'olti'
#     elif qoldiq == 7:
#         letter += 'yetti'
#     elif qoldiq == 8:
#         letter += 'sakkiz'
#     elif qoldiq == 9:
#         letter += "to'qqiz"
#     print(f"{letter} som")

# NO 11.2
# pul = int(input("pul miqdorini kiriting:"))
# if pul < 1000:
#     first_number = pul//100
#     if first_number == 1:
#         first_world = "bir yuz"
#     elif first_number == 2:
#         first_world = "ikki yuz"
#     elif first_number == 3:
#         first_world = "uch yuz"
#     elif first_number == 4:
#         first_world = "to'rt yuz"
#     elif first_number == 5:
#         first_world = "besh yuz"
#     elif first_number == 6:
#         first_world = "olti yuz"
#     elif first_number == 7:
#         first_world = "yetti yuz"
#     elif first_number == 8:
#         first_world = "sakkiz yuz"
#     elif first_number == 9:
#         first_world = "to'qqiz yuz"
#     second_number = pul//10 % 10
#     if second_number == 1:
#         second_world = "o'n"
#     elif second_number == 2:
#         second_world = "yigirma"
#     elif second_number == 3:
#         second_world = "o'ttiz"
#     elif second_number == 4:
#         second_world = "qirq"
#     elif second_number == 5:
#         second_world = "ellik"
#     elif second_number == 6:
#         second_world = "oltmish"
#     elif second_number == 7:
#         second_world = "yetmish"
#     elif second_number == 8:
#         second_world = "sakson"
#     elif second_number == 9:
#         second_world = "to'qson"
#     thirst_number = pul % 10
#     if thirst_number == 1:
#         thirst_world = "bir"
#     elif thirst_number == 2:
#         thirst_world = "ikki"
#     elif thirst_number == 3:
#         thirst_world = "uch"
#     elif thirst_number == 4:
#         thirst_world = "to'rt"
#     elif thirst_number == 5:
#         thirst_world = "besh"
#     elif thirst_number == 6:
#         thirst_world = "olti"
#     elif thirst_number == 7:
#         thirst_world = "yetti"
#     elif thirst_number == 8:
#         thirst_world = "sakkiz"
#     elif thirst_number == 9:
#         thirst_world = "to'qqiz"
#     print(first_world+" "+second_world+" "+thirst_world)
# else:
#     print("1000 dan kichik son kiritishingiz kerak")
# pul = int(input("pul miqdorini kiriting:"))
# if pul < 1000:
#     first_number = pul//100
#     if first_number == 1:
#         first_world = "bir yuz"
#     elif first_number == 2:
#         first_world = "ikki yuz"
#     elif first_number == 3:
#         first_world = "uch yuz"
#     elif first_number == 4:
#         first_world = "to'rt yuz"
#     elif first_number == 5:
#         first_world = "besh yuz"
#     elif first_number == 6:
#         first_world = "olti yuz"
#     elif first_number == 7:
#         first_world = "yetti yuz"
#     elif first_number == 8:
#         first_world = "sakkiz yuz"
#     elif first_number == 9:
#         first_world = "to'qqiz yuz"
#     second_number = pul//10 % 10
#     if second_number == 1:
#         second_world = "o'n"
#     elif second_number == 2:
#         second_world = "yigirma"
#     elif second_number == 3:
#         second_world = "o'ttiz"
#     elif second_number == 4:
#         second_world = "qirq"
#     elif second_number == 5:
#         second_world = "ellik"
#     elif second_number == 6:
#         second_world = "oltmish"
#     elif second_number == 7:
#         second_world = "yetmish"
#     elif second_number == 8:
#         second_world = "sakson"
#     elif second_number == 9:
#         second_world = "to'qson"
#     thirst_number = pul % 10
#     if thirst_number == 1:
#         thirst_world = "bir"
#     elif thirst_number == 2:
#         thirst_world = "ikki"
#     elif thirst_number == 3:
#         thirst_world = "uch"
#     elif thirst_number == 4:
#         thirst_world = "to'rt"
#     elif thirst_number == 5:
#         thirst_world = "besh"
#     elif thirst_number == 6:
#         thirst_world = "olti"
#     elif thirst_number == 7:
#         thirst_world = "yetti"
#     elif thirst_number == 8:
#         thirst_world = "sakkiz"
#     elif thirst_number == 9:
#         thirst_world = "to'qqiz"
#     print(first_world+" "+second_world+" "+thirst_world)
# else:
#     print("1000 dan kichik son kiritishingiz kerak")


# NO 12
# s = int(input("Sm."))
# if s < 0 and s <= 10:
#     print(s)
# elif s > 0 and s < 100:
#     d = s % 100
#     r = d // 10
#     f = s % 10
#     print(r, "dm", f, "sm")
# else:
#     t = s // 100
#     d = s % 100
#     r = d // 10
#     f = s % 10
#     print(t, "metr", r, "dm", f, "sm")

# No 14
# a = 4233  # sekund o'tdi
# d = a//3600
# b = a//60
# g = a % 360
# e = b-d*60
# c = g % 60
# print(d, "soat  ", e, "minut ", c, "sekund o'tdi")

# NO 15
# a = int(input("a = "))

# if a > 0 and a < 120:
#     print("To'g'ri.", a)
# else:
#     print("Bu odamga tez go'rkov kerak!!!.")


# NO 16
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))

# if a == b and a == c:
#     print('a = ', a, 'b = ', b, 'c = ', c)
# elif a == b:
#     print('a = ', a, 'b = ', b)
# elif a == c:
#     print('a = ', a, 'c = ', c)
# elif b == c:
#     print('b = ', b, 'c = ', c)
# else:
#     print("Xatolik.")


# NO 17 Loyiha

# a = int(input("Bermorning yoshi nechida? "))

# if a < 10:
#     print("123-xonada bolalar shifokori bor")
# elif a > 10:
#     b = input('Nima bezovta qilyapti? ')
#     c = "bosh og'rig'i"
#     n = "tomoq og'rig'i"
#     p = "isitma"
#     if b == c:
#         d = input(
#             "Qancha vaqtdan beri bezovta qilyapti va nimadan so'ng boshlandi?")
#         t = "1 kundan beri ishdan keyin"
#         g = "5 kundan beri yiqilishdan keyin"
#         if d == t:
#             print(
#                 "3 marta trimol tablektasini iching. Agar yordam bermasa ertaga yana keling shifokor huziriga")
#         elif d == g:
#             print(
#                 "unda birinchi boshingizni birinchi MRT ko'rigidan o'tkazing va natijasi bilan ertaga keling")
#         else:
#             print("Xatolik.")
#     elif b == n:
#         text = "1 kundan beri sovuq ichimlikdan keyin"
#         text2 = "5 kundan beri qattiq shamollashdan keyin "
#         u = input(
#             "Qancha vaqtdan beri bezovta qilyapti va nimadan so'ng boshlandi?")
#         if u == text:
#             print("1 xafta davomida Efizol tablektasini iching. Agar yordam bermasa keyingi xaftada yana keling shifokor huziriga")
#         elif u == text2:
#             print(
#                 "“unda birinchi tomog'ingizni birinchi UZI ko'rigidan o'tkazing va natijasi bilan ertaga keling.")
#         else:
#             print("Xatolik.")
#     elif b == p:
#         text3 = "1 kundan beri uyqudan keyin"
#         text4 = "5 kundan beri qattiq shamollashdan keyin"
#         f = input(
#             "Qancha vaqtdan beri bezovta qilyapti va nimadan so'ng boshlandi?")
#         if f == text3:
#             print("Hozircha sizga qo'shimcha vositalar kerak emas. Agar isitma tushmasa ertaga yana keling shifokor huziriga")
#         elif f == text4:
#             print(
#                 "unda birinchi boshingizni birinchi MRT ko'rigidan o'tkazing va natijasi bilan ertaga keling")
#         else:
#             print("Xatolik.")
#     else:
#         print("Xatolik.")
# else:
#     print("Xatolik.")
