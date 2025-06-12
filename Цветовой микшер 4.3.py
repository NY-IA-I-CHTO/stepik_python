color_one = input()
color_two = input()
red = 'красный'
blue = 'синий'
yellow = 'желтый'

if color_one == red and color_two == blue or color_one == blue and color_two == red:
    print('фиолетовый')
elif color_one == red and color_two == yellow or color_one == yellow and color_two == red:
    print('оранжевый')
elif color_one == blue and color_two == yellow or color_one == yellow and color_two == blue:
    print('зеленый')
elif color_one == color_two and (color_one == blue or color_one == red or color_one == yellow):
    print(color_one)
else:
    print('ошибка цвета')