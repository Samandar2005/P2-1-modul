# def new(mks):
#     mark = int(input('Mark = '))
#     mks.append(mark)


# marks = [67, 87, 96, 69, 74]
# new(marks)
# print(marks)


# b = {1, 2, 3, 4, 5}
# i = 0
# c = len(b)
# while i < c:
#     print(b.pop())
#     i += 1


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
#     print("Id |\tFamiliya|\tIsm\t|\tYosh | Level | Mark")
#     print('-'*60)

#     for student in talabalar:
#         for item in student:
#             print(f'{item}', end='\t')
#         print()


# current_page = 0


# def make_parts(talabalar):
#     global current_page
#     current_page = 1
#     n = len(talabalar)
#     k = 10
#     parts_count = n // k
#     print_students(talabalar[0:k+1])
#     i = 0
#     print("Qismlar: ")
#     print('<', end=' ')
#     while i < parts_count:
#         i += 1
#         print(f'{i}', end=' ')
#     if parts_count * k < n:
#         parts_count += 1
#         i += 1
#         print(f'{i}', end=' ')
#     print('>')

#     target = '1'
#     while target != '0':
#         target = input("O'tmoqchi bo'lgan qismingizni kiriting: ")
#         if target.isdigit():
#             target = int(target)
#             if target == current_page:
#                 pass
#             else:
#                 print_students(talabalar[(target-1)*k:target*k])
#                 current_page = target
#         else:
#             if target == '>' and current_page < parts_count:
#                 target = current_page + 1
#                 current_page = target
#                 print_students(talabalar[(target-1)*k:target*k])
#             elif target == '<' and current_page > 1:
#                 target = current_page - 1
#                 current_page = target
#                 print_students(talabalar[(target-1)*k:target*k])


# students = default_students()
# make_parts(students)
