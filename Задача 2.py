num = int(input('Введите число: '))     #числа 0 и 1 не являются ни простыми, ни составными
if num <= 1 or num > 100000:
    print ('Введите число больше 1, но меньше 100000!')
else:
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
    print(f'Число {num} является простым!' if flag == True else f'Число {num} является составным!')