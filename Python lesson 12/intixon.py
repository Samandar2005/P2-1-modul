# No2
def sum(n):
    while n >= 0:
        a = n % 10
        if a == 5 and n % 9 == 0:
            print("ortiqcha", n)
        n -= 1


n = int(input("n = "))
sum1 = sum(n)

# NO 3
# def user_name():
#     names = ["samandar_12", "@sasha_21", "salim_12",
#              "@sanjar_1", "@abdulla", "jamila_12"]
#     return names


# def filten_name(users):
#     filterid = []
#     for name in users:
#         i = 0
#         a = len(name)
#         if name[0] != '@' and name[a-1].find('_') == -1:
#             filterid.append(name)
#     return filterid


# users = user_name()
# names_main = filten_name(users)
# print(names_main)


# def default_students():
#     def_sts = [
#         ("Trimol", 2021, 13000, 806, 2022),
#         ("Sitramol", 2020, 106000, 708, 2022),
#         ("Validol", 2022, 13000, 707, 2024),
#         ("Yodamarin", 2019, 7400, 809, 2020),
#         ("Vitamin A", 2020, 402000, 506, 2021),
#         ("Vitamin B", 2022, 93000, 806, 2025),
#         ("Vitamin R", 2018, 150000, 607, 2021),
#         ("Vitamin T", 2004, 98000, 708, 2020),
#     ]
#     return def_sts


# def main(name):
#     i = 0
#     for item in name:
#         a = item[5] - 2
#         if item[2] <= a and item[2] >= 10000 and item[2] <= 100000:
#             print(item)
#         i += 1


# name = default_students()
# javob = main(name)
