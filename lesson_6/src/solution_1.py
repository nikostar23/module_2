def get_odd_items(products: list) -> None:
    return f"Товары с нечётными индексами: {', '.join(products[1::2])}"
    
    
print(get_odd_items(["Чай", "Кофе", "Сахар", "Молоко", "Мед"]))

print(get_odd_items(["Яблоки", "Груши", "Бананы", "Ананасы"]))
