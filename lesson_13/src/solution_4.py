def my_decorator(func):
    def wrapper(data):
        if len(data) == 2:
            if isinstance(data[0], str) and isinstance(data[1], int):
                print('Estimated time calculated successfully')
            elif not isinstance(data[0], str):
                print('Ошибка: Первый аргумент не строка!')
            elif not isinstance(data[1], int):
                print('Ошибка: Второй аргумент не число!')
        else:
            print('Ошибка: Аргументов не 2!')
        func()
    return wrapper

@my_decorator
def estimate_time() -> None:
    pass

estimate_time(('Вэб-сайт', 'пять'))
estimate_time(('Визитка', 10))
estimate_time(('Визитка', 10, 20))