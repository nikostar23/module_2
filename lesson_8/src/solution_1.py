def price_products(items: dict):
    word = input("Введите товар: ")
    if word in items:
        print("Цена: ", items[word])
    else:
        print('Товар отсутствует')

price_products({'Яблоко': 100, 'Банан': 80, 'Кофе': 250, 'Чай': 150})