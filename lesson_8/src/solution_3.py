price_products: dict[str, int] = {'Яблоко': 100, 'Банан': 80, 'Кофе': 250, 'Чай': 150}

m = max(price_products, key=price_products.get) # Выдаёт ключ с наибольшим значением

print(m) 
