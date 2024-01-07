def get_items(name_products: list, idx1: int, idx2: int):
    name_products[(idx1 - 1)], name_products[(idx2 - 1)] = name_products[(idx2 - 1)], name_products[(idx1 - 1)]
    
    return f"На полке: {', '.join(name_products)}"
    
print(get_items(["Чай", "Мед", "Сахар"], 1, 3))
