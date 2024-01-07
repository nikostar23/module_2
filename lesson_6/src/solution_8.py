def get_items(name_products: list) -> None:
    name_products[(idx1 - 1)], name_products[(idx2 - 1)] = name_products[(idx2 - 1)], name_products[(idx1 - 1)]
    
    return f"На полке: {', '.join(name_products)}"
    
idx1 = 1
idx2 = 3
print(get_items(["Чай", "Мед", "Сахар"]))

