def my_decorator(func):
    def wrapper(data):
        if data == ('Роман', 'correctpassword'):
            print('Доступ получен. Данные:...')
        elif data == ('Олег', 'wronqpassword'):
            print('В доступе отказано!')
        func()
    return wrapper

@my_decorator
def access_client_data() -> None:
    pass

access_client_data(('Роман', 'correctpassword'))
access_client_data(('Олег', 'wronqpassword'))