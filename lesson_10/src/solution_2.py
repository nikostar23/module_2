def time_fon(time: int):
    if 6 <= time < 18:
        print('Цвет фона: ', 'Светлый')
    elif 18 <= time <= 23 or 0 <= time < 6:
        print('Цвет фона: ', 'Темный')
    else:
        print("Некорректное время")

time_fon(10)
time_fon(20)
time_fon(5)