name1, name2, name3 = str(input()), str(input()), str(input())

a = len(name1)
b = len(name2)
c = len(name3)

maxi = max(a, b, c)
mini = min(a, b, c)
sr = (a + b + c) - (maxi + mini)

d = (maxi - mini) / (3 - 1)

if mini + d == sr:
    print('YES')
else:
    print('NO')