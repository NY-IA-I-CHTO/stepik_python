num = int(input())

if 0 <= num <= 36:
    if 1 <= num <= 10:
        if num % 2 == 0:
            print('черный')
        else:
            print('красный')
    elif 11 <= num <= 18:
        if num % 2 == 0:
            print('красный')
        else:
            print('черный')
    elif 19 <= num <= 28:
        if num % 2 == 0:
            print('черный')
        else:
            print('красный')
    elif 29 <= num <= 36:
        if num % 2 == 0:
            print('красный')
        else:
            print('черный')
    elif num == 0:
        print('зеленый')
else:
    print('ошибка ввода')
        
        