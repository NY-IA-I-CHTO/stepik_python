n1, n2, n3 = int(input()), int(input()), int(input())
maxi = max(n1, n2, n3)
mini = min(n1, n2, n3)

print(maxi)

if maxi == n1:
    if mini == n3:
        print(n2)
        print(mini)
    elif mini == n2:
        print(n3)
        print(mini)
elif maxi == n2:
    if mini == n3:
        print(n1)
        print(mini)
    elif mini == n1:
        print(n3)
        print(mini)
elif maxi == n3:
    if mini == n1:
        print(n2)
        print(mini)
    elif mini == n2:
        print(n1)
        print(mini)

