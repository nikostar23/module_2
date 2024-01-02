name_products: list[str] = ["Чай", "Мед", "Сахар"]
a = int(input('Введите первую позицию для замены: '))
b = int(input('Введите вторую позицию для замены: '))
temp = name_products[a]
name_products[a] = name_products[b]
name_products[b] = temp
print(name_products)
