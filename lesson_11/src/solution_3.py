stock_level = int(input('Введите уровень запаса: '))
def track_low_stock_with_for(stock: dict):
    for product, item in stock.items():
        if item < stock_level:
            print('Низкий запас: ')
            print(f'{product} - {item}')

track_low_stock_with_for({'apples': 50, 'bananas': 10, 'cherries': 3})
