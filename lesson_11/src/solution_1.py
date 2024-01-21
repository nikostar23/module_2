def sum_sales_with_for(sales: list):
    s = 0
    for i in range(len(sales)):
        s = s + sales[i]
   
    sales = ('+').join(map(str, sales))
    print('Сумма продаж: ', end='')
    print(sales, sep='+', end='=')
    print(s)

sum_sales_with_for([100, 200, 300])
sum_sales_with_for([15, 23, 39, 50])