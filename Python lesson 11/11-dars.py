# def default_students():
#     def_sts = [
#         (1, "Fayziyev", "Abdulhay", 16, 4, 86),
#         (3, "Bo'tayorov", "Karamatulloh", 21, 2, 78),
#         (4, "Najmiddinov", "Shag'zod", 23, 3, 77),
#         (5, "Amirqulov", "Amirqul", 22, 4, 89),
#         (6, "Doniyorov", "Mahmudjon", 19, 1, 56),
#         (7, "Islomov", "Jaxongir", 16, 2, 86),
#         (8, "Qobiljon", "Hudoyberdiyev", 25, 3, 67),
#         (9, "Obidov", "Khusniddin", 16, 4, 78),
#         (10, "Zohidov", "Begzod", 23, 1, 77),
#         (11, "Mirzaqulov", "Begzod", 21, 2, 89),
#         (12, "Salayev", "Zufar", 23, 3, 56),
#         (13, "Rahmatov", "Shaxboz", 22, 4, 86),
#         (14, "Azizbek", "Abdurahmonov", 19, 1, 67),
#         (15, "Ubaydullayev", "Javlonbek", 16, 2, 78),
#         (16, "Маматисаков", "Бахром", 25, 3, 77),
#         (17, "Sultonov", "Jasur", 16, 4, 89),
#         (18, "Samandar", "Bo'riyev", 23, 1, 56),
#         (19, "Muzaffar", "Muhibullayev", 21, 2, 86),
#         (20, "Musayev", "Abror", 23, 3, 67),
#         (21, "Ikromov", "Shaxzod", 22, 4, 78),
#         (22, "Dadaxanov", "Abdusattor", 19, 1, 77),
#         (23, "Begzod", "Nasirov", 16, 2, 89),
#         (24, "Nurilloh", "Anvarjonov", 25, 3, 56)
#     ]
#     return def_sts


# def print_students(talabalar):
#     print("Id |\tFamiliya |\tIsim |\tYosh | Level | Mark")
#     print('-'*60)

#     for students in talabalar:
#         for item in students:
#             print(f'{item}', end='\t')
#         print()


# curent_page = 0


# def make_page(talabalar):
#     global curent_page
#     curent_page = 1
#     n = len(talabalar)
#     k = 10
#     partes_count = n // k
#     print_students(talabalar[0:k+1])
#     i = 0
#     print("qisimlar: ")
#     print('<', end=' ')

#     while i < partes_count:
#         i += 1
#         print(f'{i}', end=' ')
#     if partes_count * k < n:
#         partes_count += 1
#         i += 1
#         print(f'{i}', end=' ')
#     print('>')

#     target = '1'

#     while target != '0':
#         target = input("O'tmoqchi bo'lgan qismingizni kiriting: ")
#         if target.isdigit():
#             target = int(target)
#             if target == curent_page:
#                 pass
#             else:
#                 print_students(talabalar[(target - 1) * k: target * k])
#                 curent_page = target
#         else:
#             if target == '>' and curent_page < partes_count:
#                 target = curent_page + 1
#                 curent_page = target
#                 print_students(talabalar[(target - 1) * k: target * k])
#             elif target == '<' and curent_page > 1:
#                 target = curent_page - 1
#                 curent_page = target
#                 print_students(talabalar[(target - 1) * k: target * k])


# students = default_students()
# make_page(students)


# -*- coding: utf-8 -*-


# NO 1
# list = []


# def qoshber():
#     """
#     Bu funksiya soz qoshish uchun ishlatiladi

#     Returns
#     -------
#     list : TYPE
#         DESCRIPTION.

#     """
# lis = input("Familya>  ")
# Ism = input("Ism> ")
# sharf = input("sharifi> ")
# age = int(input("Yoshini kiriting>> "))
# level = int(input("Darajasini kiriting>> "))
# mark = int(input("Baxosini  kiriting>> "))
# for li in lis:
# list.append(lis)
# list.append(Ism)
# list.append(sharf)
# list.append(age)
# list.append(level)
# list.append(mark)
# print(
#     f"Fam: {lis}\nIsm {Ism}\nSharifi {sharf}\nYoshi {age}\nkursi {level}\nBahosi {mark}")
# return list


# n = int(input("kirit son "))
# i = 1
# soz = 0
# while i <= n:
#     i += 1
#     soz = qoshber()
# for item in soz:
#     ali = item.sort()
# print(soz)
# print(f"Fam: {lis}\nIsm {Ism}\nSharifi {sharf}\nYoshi {age}\nkursi {level}\nBahosi {mark}")


# num = {x: x*x for x in range(8)}
# print(num)


# Uyga vazifa: mark uchun filter;
