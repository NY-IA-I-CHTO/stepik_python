ng = int(input())
mx = 1
mn = 0

for i in range(ng):
    n = int(input())
    if n > mx:
        mn = mx
        mx = n
    elif n > mn:
        mn = n

print(mx, mn, sep='\n')

