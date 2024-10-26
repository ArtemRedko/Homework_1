from random import randint
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)
for i in range(10):
    num_0 = int(input(f'Угадайте число! У вас осталось {10 - i} попыток: '))
    if num_0 > num:
        print('Меньше!')
    elif num_0 < num:
        print('Больше!')
    elif num_0 == num:
        print('Поздравляем! Вы угадали число!')
        quit()    
print('К сожалению, вы исчерпали все попытки!')