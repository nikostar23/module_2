def my_decorator(func):
    def wrapper(data):
        func()
        print(f'Цена на {data[0]} изменилась! {data[1]} > {data[2]}')
    return wrapper

@my_decorator
def change_price() -> None:
    pass

change_price(('Кресло', 5000, 4500))
change_price(('Стол', 8000, 7600))