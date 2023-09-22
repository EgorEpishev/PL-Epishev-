a=int(input('Введите число:'))
b=int(input('Введите число:'))
c = input('Введите знак + или -:')
if c == '+':
        print(a + b)
elif c == '-':
        if b > a:
                print(b - a)
        elif a>b:
                print(a - b)
        else:
                print('0')