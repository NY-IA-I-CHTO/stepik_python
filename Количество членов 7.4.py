text = input()
total = 0
while text != 'стоп' and text != 'хватит' and text != 'достаточно':
    text = input()
    total += 1
print(total)