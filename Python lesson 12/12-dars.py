
def default_students():
    def_sts = [
        (1, "Samsung", "Galaxiy A12", 4, 6.5, 128),
        (2, "Samsung", "Galaxiy A52", 4, 6.5, 64),
        (3, "Samsung", "Galaxiy S21", 8, 6.2, 128),
        (4, "Samsung", "Galaxiy S20", 6, 6.5, 128),
        (5, "Samsung", "Galaxiy A12", 6, 6.5, 32),
        (6, "Xiomi", "Redmi 9C", 3, 6.5, 68),
        (7, "Samsung", "Galaxiy A32", 4, 6.4, 64),
        (8, "Samsung", "Galaxiy A22", 4, 6.5, 64),
        (9, "iPhone ", "13 Pro Max", 6, 6.7, 128),
        (10, "Samsung", "Galaxiy A02", 2, 6.5, 32),
        (11, "Samsung", "Galaxiy S21", 12, 6.8, 256),
        (12, "Samsung", "Galaxiy M12", 3, 6.5, 32),
        (13, "Apple", "iPhone 11", 4, 6.1, 128),
    ]
    return def_sts


def print_students(talabalar):
    print("Id |\tKompaniya|\tRusum\t|\tO.Xotira | Dyuym | Xotira hajmi")
    print('-'*60)

    for student in talabalar:
        for item in student:
            print(f'{item}', end='\t')
        print()


current_page = 0


def make_parts(talabalar):
    global current_page
    current_page = 1
    n = len(talabalar)
    k = 10
    parts_count = n // k
    print_students(talabalar[0:k+1])
    i = 0
    print("Qismlar: ")
    print('<', end=' ')
    while i < parts_count:
        i += 1
        print(f'{i}', end=' ')
    if parts_count * k < n:
        parts_count += 1
        i += 1
        print(f'{i}', end=' ')
    print('>')

    target = '1'
    while target != 0:
        target = input("O'tmoqchi bo'lgan qismingizni kiriting: ")
        if target.isdigit():
            target = int(target)
            if target == current_page:
                pass
            else:
                print_students(talabalar[(target-1)*k:target*k])
                current_page = target
        else:
            if target == '>' and current_page < parts_count:
                target = current_page + 1
                current_page = target
                print_students(talabalar[(target-1)*k:target*k])
            elif target == '<' and current_page > 1:
                target = current_page - 1
                current_page = target
                print_students(talabalar[(target-1)*k:target*k])


def create_students(n):
    talabalar = []
    for id in range(n):
        id += 1
        fam = input("Kompaniya: ")
        isim = input("Rusum: ")
        yosh = int(input("O.Xotira: "))
        level = int(input("Dyuym: "))
        mark = int(input("Xotira hajmi: "))

        talaba = (id, fam, isim, yosh, level, mark)
        talabalar.append(talaba)
    return talabalar


students = default_students()
#students = create_students(2)
make_parts(students)


def FilterByFamIsim():
    filtered = []
    part_text = input("Enter the text: ")
    part_text = part_text.lower()
    for talaba in students:
        if talaba[1].lower().find(part_text) != -1 or \
           talaba[2].lower().find(part_text) != -1:
            filtered.append(talaba)
    return filtered


def FilterByAge():
    filtered = []

    from_age = int(input("From O.Xotira:  "))
    to_age = int(input("To O.Xotira:  "))
    for talaba in students:
        if from_age <= talaba[3] and talaba[3] <= to_age:
            filtered.append(talaba)
    return filtered


def FilterByLevel():
    filtered = []
    level = int(input("Duyum: "))
    for talaba in students:
        if talaba[4] == level:
            filtered.append(talaba)
    return filtered


def FilterByMark():
    filtered = []
    from_makr = int(input("From Xotira xajmi:  "))
    to_makr = int(input("To Xotira xajmi:  "))
    for talaba in students:
        if from_makr <= talaba[3] and talaba[3] <= to_makr:
            filtered.append(talaba)
    return filtered


filterid_by_fam = FilterByFamIsim()
filterid_by_mark = FilterByMark()
# union_list = list(set(filterid_by_fam + filterid_by_mark))
# make_parts(union_list)
