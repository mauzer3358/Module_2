numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def Proverka(Result_Pairs):
    z = len(Result_Pairs) - 1
    unik = []
    if z == 0:
        unik.append(Result_Pairs[0])
    for i in range(z):
        a = Result_Pairs[i][0]
        b = Result_Pairs[i][1]
        if a == b:
            continue
        unik.append(Result_Pairs[i])
        if len(unik) > 2:
            g = unik[-2][0]
            h = unik[-2][1]
            if unik[-1][0] == h and unik[-1][1] == g:
                del unik[-1]

    f = len(unik)
    if f > 2:
        for x in range(len(unik)):
            y = x + 1
            while y < len(unik):
                if unik[x][0] == unik[y][1] and unik[x][1] == unik[y][0]:
                    del unik[y]
                y += 1
    return unik


def Pairs(list_2):
    list_pairs_ = []
    for k in range(len(list_2)):
        for m in range(len(list_2)):
            if m == 0:
                continue
            b = list_2[k]
            c = list_2[m]
            if num % (b + c) == 0:
                list_pairs_.append([list_2[k], list_2[m]])
    return list_pairs_


def Term_list(num_1):
    list_1 = []  # list_1 - список множителей
    j = 1
    while j < num_1:
        list_1.append(j)
        j += 1  # list_1 - список множителей
    a = list_1
    return a


for var_1 in range(len(numbers)):
    num = numbers[var_1]
    num_1 = num + 1
    list_2 = Term_list(num_1)
    # print('Слагаемые', list_2)
    Result_Pairs = Pairs(list_2)
    # print('пары', Result_Pairs)
    final_pairs = Proverka(Result_Pairs)
    q = (sum(final_pairs, []))
    num_str = str(num)
    print(num_str + '- ' + ''.join(str(el) for el in q))
