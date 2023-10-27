# №1
N = int(98)
def zero(N):
    sum = 0
    for i in range(len(str(N))):
        sum = int(str(N)[i]) + sum
    N = N - sum
    return N
count = 0
while N != 0:
    N = zero(N)
    count += 1
print(count)


# №2
lst1 = [20, 30, 40]
lst2 = [35, 85, 125]
lst3 = [18, 47, 33]
def multpl(a):
    count = 1
    for i in range(len(a)):
        count = count * int(str(a[i]))
    return count
def ar_m(a):
    count = 0
    for i in range(len(a)):
        count = count + int(str(a[i]))
    return count // len(a)
print(multpl(lst1))
print(multpl(lst2))
print(multpl(lst3))
print(ar_m(lst1))
print(ar_m(lst2))
print(ar_m(lst3))

