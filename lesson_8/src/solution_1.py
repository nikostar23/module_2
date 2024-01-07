price_products: dict[str, int] = {'Яблоко': 100, 'Банан': 80, 'Кофе': 250, 'Чай': 150}
word = input("Введите товар: ")
print("Цена: ", price_products[word])
