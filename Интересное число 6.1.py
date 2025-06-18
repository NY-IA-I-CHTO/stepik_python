num = int(input())

a = num // 100
b = num // 10 % 10
c = num % 10
sr = max(a, b, c) - min(a, b, c)

if a == 0 and b == 0 or a == 0 and c == 0 or b == 0 and c == 0:
    print('Число неинтересное')
elif sr == a:
    if max(a, b, c) - min (a, b, c) == a:
        print('Число интересное')
    else:
        print('Число неинтересное')
elif sr == b:
    if max(a, b, c) - min (a, b, c) == b:
        print('Число интересное')
    else:
        print('Число неинтересное')
elif sr == c:
    if max(a, b, c) - min (a, b, c) == c:
        print('Число интересное')
    else:
        print('Число неинтересное')
else:
    print('Число неинтересное')