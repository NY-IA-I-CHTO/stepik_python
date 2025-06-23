n = int(input())
n1 = 0
n2 = 1
n3 = 1

if n == 1:
    print(1)
else:
    print(1, end=' ')
    for i in range(n - 1):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3, end=' ')


# n = int(input())
# a, b = 1, 1

# for i in range(n):
#     print(a, end=' ')
#     a, b = b, a + b