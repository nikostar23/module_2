def get_items(price_products: list) -> None:
    max_price = price_products.index(max(price_products))
    min_price = price_products.index(min(price_products))
    price_products[max_price], price_products[min_price] = min(price_products), max(price_products)
    
    return f"Новые цены: {(price_products)}"
    
    
print(get_items([10, 30, 40, 50]))

print(get_items([5, 10, 15, 25, 20]))

