def shops(items_1: str, items_2: str):
    a = items_1.split(', ')
    a = set(a)
    b = items_2.split(', ')
    b = set(b)
    c = a - b
    print('Только в первом магазине: ', c)
    d = b - a
    print('Только во втором магазине: ', d)
        
shops('Хлеб, Молоко, Сыр', 'Молоко, Йогурт, Сок')
shops('Кофе, Чай, Сахар', 'Какао, Чай, Сгущенка')