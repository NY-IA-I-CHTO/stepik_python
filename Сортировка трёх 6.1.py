n1, n2, n3 = int(input()), int(input()), int(input())
max = max(n1, n2, n3)
min = min(n1, n2, n3)
if max != n1 and min != n1:
    print(max, n3, min, sep='\n') 
elif max != n2 and min != n1:
    print(max, n1, min, sep='\n')
elif max != n3 and min != n2:
    print(max, n2, min, sep='\n')