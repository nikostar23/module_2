data = ['Кресло', 5000, 4500]
data = ['Стол', 8000, 7600]

def my_decorator(func):
    def wrapper():
        func()
        print(f'Цена на {data[0]} изменилась! {data[1]} > {data[2]}')
    return wrapper()

@my_decorator
def change_price() -> None:
    pass

change_price()
