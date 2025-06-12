a = int(input())
b = int(input())
oper = input()

if oper == '+':
    print(a + b)
elif oper == '-':
    print(a - b)
elif oper == '*':
    print(a * b)
elif oper == '/' and b != 0:
    print(a / b)
elif oper == '/':
    if b != 0:
        print(a / b)
    else:
        print('На ноль делить нельзя!')
else:
    print('Неверная операция')
