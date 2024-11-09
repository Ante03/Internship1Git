
def permutacije_brojeva(prvi, zadnji, niz):
    if prvi == zadnji:
        print(niz)
    else:
        for i in range(prvi, zadnji + 1):
            niz[i], niz[prvi] = niz[prvi], niz[i]
            permutacije_brojeva(prvi + 1, zadnji, niz)
            niz[i], niz[prvi] = niz[prvi], niz[i]


def main():
    niz = list(map(int, input("Unesite niz cijelih brojeva, odvojenih razmacima: ").split()))
    permutacije_brojeva(0, len(niz) - 1, niz)


if __name__ == '__main__':
    main()