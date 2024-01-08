def price_products(products: dict):
    m = max(products, key=products.get)
    n = min(products, key=products.get)
    print('Самый дорогой: ', m, '-', products[m], 'руб.')
    print('Самый дешевый: ', n, '-', products[n], 'руб.')

price_products({'Яблоко': 100, 'Банан': 80, 'Кофе': 250, 'Чай': 150})