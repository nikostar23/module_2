order1 = {'id': 1, 'items': ['book', 'pen']}
order2 = {'id': 2, 'items': []}

def check_order(check: dict):
    return bool(check.get('items'))

def package_order(check):  
    return bool(check)

def send_order(check_function, package_function, check: dict):
    if check_function(check):
        if package_function(check):
            return f"Отправка: Упакован заказ {check.get('id')}"
    else:
        return f"Отправка: Заказ {check.get('id')} пуст"

print(send_order(check_order, package_order, order1))
print(send_order(check_order, package_order, order2))
