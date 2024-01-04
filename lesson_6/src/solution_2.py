def get_odd_items(price_products: list) -> None:
    return f"Цены с нечётными индексами: {(price_products[1::2])}"
    
    
print(get_odd_items([50, 45, 30, 25]))

print(get_odd_items([100, 90, 85, 70, 60]))

