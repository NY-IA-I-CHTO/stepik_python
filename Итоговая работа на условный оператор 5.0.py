## Начало столетия

# year = int(input())
# y1 = year % 10
# y2 = year % 100 // 10
# if y1 == 0 and y2 == 0:
#     print('YES')
# else:
#     print('NO')



## Шахматная доска

# x = int(input())
# y = int(input())
# a = int(input())
# b = int(input())

# if (x + y) % 2 == 0:
#     YES1 = 1
# else:
#     YES1 = 0
# if (a + b) % 2 == 0:
#     YES2 = 1
# else:
#     YES2 = 0
# if YES1 == YES2:
#     print('YES')
# else:
#     print('NO')



## Girls only

# age = int(input())
# pol = input()

# if 10 <= age <= 15:
#     if pol == 'f':
#         print('YES')
#     else:
#         print('NO')
# else:
#     print('NO')



## Римские цифры

# num = int(input())
# if 1 <= num <= 10:
#     if num == 1: print('I')
#     if num == 2: print('II')
#     if num == 3: print('III')
#     if num == 4: print('IV')
#     if num == 5: print('V')
#     if num == 6: print('VI')
#     if num == 7: print('VII')
#     if num == 8: print('VIII')
#     if num == 9: print('IX')
#     if num == 10: print('X')
# else:
#     print('ошибка')



## YES or NO - вот в чём вопрос?

# num = int(input())

# if num % 2 != 0:
#     print('YES')
# elif num % 2 == 0 and 2 <= num <= 5:
#     print('NO')
# elif num % 2 == 0 and 6 <= num <= 20:
#     print('YES')
# elif num % 2 == 0 and num > 20:
#     print('NO')



## Ход слона

# str1, stl1, str2, stl2 = int(input()), int(input()), int(input()), int(input())

# if (str1 + stl1) % 2 == 0:
#     if (str2 + stl2) % 2 == 0:
#         print('YES')
#     else:
#         print('NO')
# elif (str1 + stl1) % 2 != 0:
#     if (str2 + stl2) % 2 != 0:
#         print('YES')
#     else:
#         print('NO')
# else:
#     print('NO')



## Ход коня

str1, stl1, str2, stl2 = int(input()), int(input()), int(input()), int(input())
YES = 0
if str1 < str2:
    if (str1 - 2 or str1 + 2) != str2:
        YES += 1
    elif (str1 - 1 or str1 + 1) != str2:
        YES += 1
    elif YES == 2:
        print('NO')
elif stl1 < stl2:
    if (stl1 - 2 or stl1 + 2) != stl2:
        YES += 1
    elif (stl1 - 1 or stl1 + 1) != stl2:
        YES += 1
elif YES == 4:
    print('YES')
else:
    print('YES')
        

