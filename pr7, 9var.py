# №1
n = 98

def summ(n):
    return sum(int(digit) for digit in str(n))

def find_steps_to_zero(n):

    steps = 0
    while n != 0:
        n -= summ(n)
        steps += 1
    return steps

print(find_steps_to_zero(n))


# №2
lst1 = [20, 30, 40]
lst2 = [35, 85, 125]
lst3 = [18, 47, 33]
multpl1 = 1
for i in lst1:
    multpl1 *= i
multpl2 = 1
for i in lst2:
    multpl2 *= i
multpl3 = 1
for i in lst3:
    multpl3 *= i
ar_m1 = sum(lst1) / len(lst1)
ar_m2 = sum(lst2) / len(lst2)
ar_m3 = sum(lst3) / len(lst3)

print("Произведение элементов первого массива:", multpl1)
print("Среднее арифметическое значение первого массива:", ar_m1)
print("Произведение элементов второго массива:", multpl2)
print("Среднее арифметическое значение второго массива:", ar_m2)
print("Произведение элементов третьего массива:", multpl3)
print("Среднее арифметическое значение третьего массива:", ar_m3)

