data = []

def my_decorator(func):
    def wrapper(*args):
        global data
        num = None
        if data != args:
            num = func(*args)
            data = args
            print(f'Посчитали цену: {num}')
        
        else:
            num = func(*args)
            print(f'Загрузили из кэша: {num}')
    return wrapper

@my_decorator
def calculate_project_cost(*args):
    return 3000

calculate_project_cost(['Логотип', 'малый бизнес'])
calculate_project_cost(['Логотип', 'малый бизнес'])