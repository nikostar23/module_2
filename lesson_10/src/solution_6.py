def find_max_price(price, max_price = None):
    if max_price == None:
        max_price = price.pop()
    a = price.pop()

    if a > max_price:
        max_price = a
    
    if price:
        return find_max_price(price, max_price)
    return max_price

find_max = [15, 7, 9]
find_max = [1, 10, 20, 5]
find_max = [25, 25, 25]
find_max = [10, 8, 12]
result = find_max_price(find_max)
print(result)
