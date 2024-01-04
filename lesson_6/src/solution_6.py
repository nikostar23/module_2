name_products: list[str] = ["Чай", "Кофе", "Сахар"]
new_product_num = int(input("Введите номер позиции для нового товара: "))
new_product = input("Введите новый товар: ")

name_products.insert((new_product_num - 1), new_product)
print("Товары на полке: ", ', '.join(name_products))
