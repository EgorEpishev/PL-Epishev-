# №1
from random import randint
n = int(input("Введите порядок n: "))
a = 1
b = 9
k = int(input("Введите число k: "))
lst_0 = []
print("Матрица: ")
for i in range(n):
    lst_1 = []
    for j in range(n):
        lst_1.append(int(randint(a, b)))
        print(lst_1[j], end=' ')
    lst_0.append(lst_1)
    print()
def div(lst_0, k):
    diag_el = lst_0[k-1][k-1]
    for j in range(len(lst_0[k-1])):
        lst_0[k-1][j] /= diag_el
    return lst_0
print("Матрица с преобразованием: ")
i = div(lst_0, k)
for i in range(n):
    for j in range(n):
        print(lst_0[i][j], end=' ')
    print()

# №2
a = [[0, 5, 88], [67, 0, 15], [77, 23, 0]]
for i in a:
    print(i)
print()
n = 3
b = []
for i in range(n):
    b.append([0] * n)
for i in range(n):
    for j in range(n):
        b[j][i] = a[i][j]
for i in range(len(b)):
    print(b[i])
