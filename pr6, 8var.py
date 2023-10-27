# №1
lst = [89, 50, 32, 10, 4, 106]
lst_sum = 0
lst_prod = 1
for i in lst:
    lst_sum += i
    lst_prod *= i
print("Исходный список:", lst)
print("Сумма элементов списка =", lst_sum)
print("Произведение элементов списка =", lst_prod)

# №2
lst = [1, 2.34, -5, 0, 10, 25, 0]
lst_sum = sum(lst)
lst_mid = sum(lst) / len(lst)
for i in range(len(lst)):
    if lst[i] == 0:
       lst[i] = lst_mid
print(lst)
