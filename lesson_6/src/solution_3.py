def get_lactose_items(products: list) -> None:
    lactose = "Молоко" in products
    return f"В товарах есть молоко: {(lactose)}"
    
    
print(get_lactose_items(["Чай", "Кофе", "Сахар", "Молоко", "Мед"]))

print(get_lactose_items(["Яблоки", "Груши", "Бананы", "Ананасы"]))

