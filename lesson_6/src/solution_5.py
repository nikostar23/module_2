price_products: list[int] = [10, 30, 40, 50]
a = max(price_products)
b = min(price_products)
n = len(price_products)
t1 = 0
t2 = 0
for i in range(n):
    if price_products[i] == a:
       t1 = i
    if price_products[i] == b:
       t2 = i
tepm = price_products[t1]
price_products[t1] = price_products[t2]
price_products[t2] = tepm
          
print(price_products)

price_products: list[int] = [5, 10, 15, 25, 20]
a = max(price_products)
b = min(price_products)
n = len(price_products)
t1 = 0
t2 = 0
for i in range(n):
    if price_products[i] == a:
       t1 = i
    if price_products[i] == b:
       t2 = i
tepm = price_products[t1]
price_products[t1] = price_products[t2]
price_products[t2] = tepm
          
print(price_products)