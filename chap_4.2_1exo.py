n = int(input())
m = 2 * n


def catalan(n):
    i = 1
    ii = 1
    iii = 1
    deuxnfac = 1
    nfacone = 1
    nfac = 1
    while i < m:
        deuxnfac = deuxnfac * (i + 1)
        i = i + 1
    while ii < n + 1:
        nfacone = nfacone * (ii + 1)
        ii = ii + 1
    while iii < n:
        nfac = nfac * (iii + 1)
        iii = iii + 1

    return (deuxnfac / (nfacone * nfac))

print(catalan(n))