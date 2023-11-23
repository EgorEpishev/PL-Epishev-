file = open('C:\\Users\\user\\Desktop\\проги\\Практики.ЯП\\ввод матрицы.txt', 'r')
a = []
for j in file:
    a.append(j.split())
file.close()

c = []
for i in a:
    b = []
    for j in i:
        b.append(int(j))
    c.append(b)
s = []
for i in range(len(c)):
    s.append(sum(c[i]))

file = open("C:\\Users\\user\\Desktop\\проги\\Практики.ЯП\\вывод матрицы.txt", 'w', encoding= 'utf-8')
file.write("Строка с наибольшей суммой:")
for k in c[s.index(max(s))]:
    file.write(str(k))
    file.write(' ')
file.write("\nСумма элементов: ")
file.write(str(max(s)))
file.write("\nСтрока с наименьшей суммой: ")
for g in c[s.index(min(s))]:
    file.write(str(g))
    file.write(' ')
file.write("\nСумма элементов: ")
file.write(str(min(s)))
