def update_stock(item: str, quantity: int, stock: dict):
    if item in stock:
        stock[item]['quantity'] += quantity
    
    else:
        stock[item] = {'quantity': quantity}
    

def get_item_quantity(item_name, stock: dict):
    if item_name in stock:
        return stock[item_name]['quantity']
    else:
        return 0


def remove_item(item, stock):
    if item in stock:
        del stock[item]

stock = {}

update_stock('Apple', 50, stock)
update_stock('Banana', 30, stock)
update_stock('Coffee', 20, stock)

print(get_item_quantity('Apple', stock))

remove_item('Banana', stock)

print(stock)