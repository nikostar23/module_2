def calculate_discount(price: str):
    a = price.split(', ')
    price_1 = int(a[0])
    price_2 = int(a[1])
    price_3 = int(a[2])
    discount = int(a[3])
    print('Сумма скидки: ', int((price_1 + price_2 + price_3) * discount / 100))
     
calculate_discount('100, 200, 300, 10')
calculate_discount('50, 150, 250, 20')
