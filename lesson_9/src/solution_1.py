def calculate_discount(price: list):
    discount = price.pop()
    
    summ = sum(price)
    
    print('Сумма скидки: ', summ * discount / 100)
     
calculate_discount([100, 200, 300, 10])
calculate_discount([50, 150, 250, 20])
