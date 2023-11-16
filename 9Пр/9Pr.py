# Блок А, №4
def summ(N):
    if N < 10:
        return N
    else:
        return N % 10 + summ(N // 10)


N = int(input('Введите натуральное число N: '))
print('Сумма цифр числа N: ', summ(N))



# Блок Б, №2
lst = []
def sec_max():
    n = int(input())
    if n == 0:
        return 0
    lst.append(n)
    return sec_max()

sec_max()
lst.sort()
print(lst[-2])