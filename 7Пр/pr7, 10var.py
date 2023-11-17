# №1
from random import randint
N = randint(210, 231) 
count = 0
def num(one, ten, hun):
    if one != ten and ten != hun and one != hun:
        return True
for i in range(100, N + 1):
    if num(i // 100, (i // 10)%10, i%10):
        count += 1
        print(i)
print(count)



# №2
def str_rvs (str):
    word = str.split()
    str_rvs  = ' '.join(reversed(word))
    return str_rvs

str = input('Введите строку:')
print('Результат:', str_rvs(str))
