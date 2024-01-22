def count_specific_items_with_while(products: list, product):
    s = 0
    i = 0
    while i < len(products):
        if products[i] == product:
            s = s + 1
        
        i = i + 1
    print(f'Количество \'{product}\': {s}')

count_specific_items_with_while(['fruit', 'toy', 'fruit', 'toy'], 'toy')
count_specific_items_with_while(['clotes', 'clotes', 'clotes'], 'clotes')


# так можно сделать через .count()
#product = input('Введите наименование товара: ')
#def count_specific_items_with_while(products: list):
#    s = products.count(product)
#    print(s)

#count_specific_items_with_while(['fruit', 'toy', 'fruit', 'toy', 'toy'])
