data_1 = ['Роман', 'correctpassword']
data_2 = ['Олег', 'wronqpassword']

def my_decorator(func):
    def wrapper():
        if data_1:
            print('Доступ получен. Данные:...')
        if data_2:
            print('В доступе отказано!')
        func()
    return wrapper()

@my_decorator
def access_client_data() -> None:
    pass

access_client_data()