def get_items(name_products: list) -> None:
    name_1 = int(input("Введите позицию перестановки первого товара: "))
    name_2 = int(input("Введите позицию перестановки второго товара: "))
    
    name_products[(name_1 - 1)], name_products[(name_2 - 1)] = name_products[(name_2 - 1)], name_products[(name_1 - 1)]
    
    return f"На полке: {', '.join(name_products)}"
    
    
print(get_items(["Чай", "Мед", "Сахар"]))

