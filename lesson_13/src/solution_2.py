data_1 = ['Логотип Васильевский рынок']
data_2 = ['Макет сайта Логомашины']

def my_decorator(func):
    def wrapper():
        func()
        if data_1:
            print('Executions: 2,45 seconds')
        if data_2:
            print('Executions: 4,30 seconds')
    return wrapper()

@my_decorator
def create_design() -> None:
    pass

create_design()