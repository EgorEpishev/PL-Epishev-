lst = [0, 1]
N, K = int(input('Введите число:')), int(input('Введите число:')) - 1
for i in range(1, N + 1):
    lst.append(lst[-2] + lst[-1])
print(sum(lst[K: len(lst)]))
