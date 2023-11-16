# №1
n = int(input("Введите размер матрицы: "))
lst = []
for i in range(n):
    row = []
    for j in range(n):
        element = int(input(f"Введите элементы матрицы [{i}][{j}]: "))
        row.append(element)
    lst.append(row)

k = int(input("Введите номер строки k: "))

diag_el = lst[k-1][k-1]

for j in range(n):
    lst[k-1][j] /= diag_el

print("Результат:")
for row in lst:
    print(row)


# №2
n = int(input("Размер матрицы: "))
A = []
for i in range(n):
    B = []
    for j in range(n):
        B.append(int(input()))
    A.append(B)

for i in range(n):
    for j in range(n):
        p = A[i][j]
        m = A[j][i]
        if i < j:
            A[i][j] = m
        if j > i:
            A[j][i] = p

for i in range(n):
    for j in range(n):
        print(A[i][j], end=" ")
    print()
