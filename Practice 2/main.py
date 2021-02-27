def f21(x):
    if x[3] == 1960:
        return 12
    elif x[3] == 1999:
        return 11
    elif x[3] == 1973:
        if x[0] == 1996:
            return 6
        elif x[0] == 2019:
            if x[4] == 1995:
                return 7
            elif x[4] == 1974:
                return 10
            elif x[4] == 1964:
                if x[1] == 2017:
                    return 8
                elif x[1] == 1963:
                    return 9
        elif x[0] == 2004:
            if x[2] == 2018:
                return 5
            elif x[4] == 1995:
                return 2
            elif x[4] == 1964:
                return 3
            elif x[4] == 1974:
                return 4
            elif x[1] == 2017:
                return 0
            elif x[1] == 1963:
                return 1


def f22(x):
    res = 0
    a = x & 0b0000_0000_0000_0000_0000_0000_0000_0001
    b = x & 0b0000_0000_0000_0001_1111_1111_1111_1110
    c = x & 0b0000_0000_0011_1110_0000_0000_0000_0000
    d = x & 0b0000_0000_0100_0000_0000_0000_0000_0000
    e = x & 0b0000_0011_1000_0000_0000_0000_0000_0000
    f = x & 0b0111_1100_0000_0000_0000_0000_0000_0000
    g = x & 0b1000_0000_0000_0000_0000_0000_0000_0000

    res = (g >> 31) | (b >> 0) | (e >> 6) | (a << 20) | (d >> 1) | (f >> 4) | (c << 10)
    return res


def f23(table):
    res_table = []
    tmp_line = []
    empty_lines = []
    empty_columns = []
    duplicates_list = []
    duplicates = {}
    n = len(table)  # Height
    m = len(table[0])  # Width
    counter_lines = 0
    counter_columns = 0
    # Search an empty line
    for i in range(n):
        for j in range(m):
            if table[i][j] is None:
                counter_lines += 1
        if counter_lines == m:
            empty_lines.append(i)
        counter_lines = 0
    # Search an empty column
    for i in range(m):
        for j in range(n):
            if table[j][i] is None:
                counter_columns += 1
        if counter_columns == n:
            empty_columns.append(i)
        counter_columns = 0

    for i in range(n):
        if tuple(table[i]) in duplicates.keys():
            duplicates_list.append(i)
        else:
            duplicates[tuple(table[i])] = 1

    # Create result table
    for i in range(m):
        for j in range(n):
            if j not in empty_lines and i not in empty_columns and j not in duplicates_list:
                tmp_line.append(table[j][i])
        if i not in empty_columns:
            res_table.append(tmp_line.copy())
        tmp_line.clear()

    n = len(res_table)
    m = len(res_table[0])

    for i in range(n):
        for j in range(m):
            if i == 0:
                res_table[i][j] = res_table[i][j].replace(".", "-")
            elif i == 1:
                res_table[i][j] = res_table[i][j].replace("@", "[at]")
            elif i == 2:
                tmp_str = res_table[i][j]
                res = tmp_str[0]
                k = 1
                while tmp_str[k] != " ":
                    k += 1

                res = res + "." + tmp_str[k + 1:]
                res_table[i][j] = res

    return res_table


table1 = [[None, None, "20.04.01", "vsevolod60@rambler.ru", "Всеволод Е. Гузедян"],
          [None, None, "23.10.00", "sufemin91@mail.ru", "Лев У. Суфемин"],
          [None, None, "09.02.03", "cazerij77@yandex.ru", "Захар Л. Чазерий"],
          [None, None, None, None, None],
          [None, None, "24.11.01", "aroslav86@mail.ru", "Ярослав З. Ницисов"],
          [None, None, None, None, None],
          [None, None, "23.10.00", "sufemin91@mail.ru", "Лев У. Суфемин"]
          ]

table2 = [[None, None, "08.05.02", "grigorij80@gmail.ru", "Григорий Ш. Тифук"],
          [None, None, None, None, None],
          [None, None, "16.08.99", "timofej16@yahoo.ru", "Тимофей Н. Мегушич"],
          [None, None, "16.08.99", "timofej16@yahoo.ru", "Тимофей Н. Мегушич"],
          [None, None, None, None, None],
          [None, None, "05.11.00", "daniel_48@yahoo.ru", "Даниэль Ф. Шекьан"]
          ]

print(f23(table1))
print(f23(table2))
