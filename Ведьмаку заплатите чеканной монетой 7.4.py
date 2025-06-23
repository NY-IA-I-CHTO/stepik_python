n = int(input())
counter = 0

while  n >= 25:
    n -= 25
    counter += 1
while n >= 10:
    n -= 10
    counter += 1
while n >= 5:
    n -= 5
    counter += 1
while n >= 1:
    n -= 1
    counter += 1

print(counter)
    
