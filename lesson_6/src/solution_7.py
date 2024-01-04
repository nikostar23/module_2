name_products: list[str] = ["Чай", "Кофе", "Сахар", "Мед"]
product_num = int(input("Позиция для удаления товара: "))

name_products.pop((product_num - 1))
print("Товары на полке: ", ', '.join(name_products))
