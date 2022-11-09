# NO 1
def dino(n):
    for i in range(0, n):
        for j in range(n, i, -1):
            print("* ", end="")
        print()


def diamond(n):
    for m in range(0, n):
        for i in range(0, m+1):
            print("* ", end="")
        print("\r")


n = int(input("son kiriting>>> "))
dino(n // 2)
diamond(n // 2)


# NO 2
# def sum(n):
#     while n >= 0:
#         a = n % 10
#         if a == 2 and n % 7 == 0:
#             print(n)
#         n -= 1


# n = int(input("n = "))
# sum1 = sum(n)

# NO 3
def familia(talabalar_familiyasi, text):
    for i in talabalar_familiyasi:
        if i.lower().startswith(text.lower()):
            print(i)


talabalar = ['Abidov', 'Akbarov', 'Arslanov', 'Buriev', 'Davlatov',
             'Erkinov', 'Furqatov', 'Ganiev', 'Hakimov', 'Tursunov']

n = input("Familiyani qidirish:")

familia(talabalar, n)
