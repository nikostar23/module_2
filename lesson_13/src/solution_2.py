import time

def my_decorator(func):
    def wrapper(data):
        start = time.time()
        func(data)
        end = time.time()
        print(f'Executions: {end - start} seconds')
        
    return wrapper

@my_decorator
def create_design(data):
    if data == 'Логотип Васильевский рынок':
        time.sleep(2.45)
    elif data == 'Макет сайта Логомашины':
        time.sleep(4.30)
    pass

create_design('Логотип Васильевский рынок')
create_design('Макет сайта Логомашины')