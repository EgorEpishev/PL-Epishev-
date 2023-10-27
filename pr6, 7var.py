# №1
lst = [3, 4, 6, 90, 45, 12]
summ = 0
multpl = 1
for i in range(len(lst)):
    if i % 2 == 0:
        summ += lst[i]
    else:
        multpl *= lst[i]
print(summ, multpl)


# №2
lst = [56, 100, -120, -300, 450, 555]
a = 0        # Минимальное число
b = 0        # Максимальное число
for i in range(len(lst)):
    if lst[i] <= min(lst):
        a = i
    elif lst[i] >= max(lst):
        b = i
lst[a], lst[b] = lst[b], lst[a]
print(lst)
