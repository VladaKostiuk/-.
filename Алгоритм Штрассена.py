import random


def matrixmult(n1, n2):
    s = 0  # сума
    t = []  # тимчасова матриця
    n3 = []  # кінцева матрица
    if len(n2) != len(n1[0]):
        print "Матриці не можуть бути перемножені"
    else:
        r1 = len(n1)  # кількість рядків у першій матриці
        c1 = len(n1[0])  # Количество стовбців в 1
        r2 = c1  # і рядків в 2ій матриці
        c2 = len(n2[0])  # кількість стовпців у 2ій матриці
        for z in range(0, r1):
            for j in range(0, c2):
                for i in range(0, c1):
                    s = s + m1[z][i] * n2[i][j]
                t.append(s)
                s = 0
            n3.append(t)
            t = []
    return n3


def creatematrix(r, c):
    t = []
    n = []
    for i in range(0, r):
        for j in range(0, c):
            t.append(random.randint(1, 10))
        m.append(t)
        t = []
    return m


c1 = 1
r2 = 2
while c1 != r2:
    print("Кількість стовпців у першому матриці має бути = кол-ті рядків 2 матриці")
    r1 = input('Введіть кількість рядків для першої матриці >')
    c1 = input('Введіть кількість стовпців для 1 матриці>')
    r2 = input('Введіть кількість рядків для другої матриці >')
    c2 = input('Введіть кількість стовпців для 2 матриці >')

n1 = creatematrix(r1, c1)
n2 = creatematrix(r2, c2)

print(n1)
print(n2)

n3 = matrixmult(n1, n2)
print n3
