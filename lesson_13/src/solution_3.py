data = []
data_1 = ['Логотип', 'малый бизнес']
data_2 = ['Логотип', 'малый бизнес']

def my_decorator(func):
    def wrapper():
        func()
        if data_1:
            data = data_1
            print('Посчитали цену: 3000')
        if data == data_2:
            print('Загрузили из кэша: 3000')
    return wrapper()

@my_decorator
def calculate_project_cost() -> None:
    pass

calculate_project_cost()