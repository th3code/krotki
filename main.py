krotka1 = (1, 2, 3, 4, 5,)
krotka2 = (5, 4, 1,)


def sprawdz(k1, k2):
    licznik = 0
    for x in k2:
        for y in k1:
            if x == y:
                licznik += 1

    if licznik == len(krotka2):
        return True
    else:
        return False


print(sprawdz(krotka1, krotka2))
