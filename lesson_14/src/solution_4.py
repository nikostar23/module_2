a = int(input('Введите количество устанавливаемых цен: '))

def fib_price(n):
    a, b = 1, 2
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fib_price(a)))