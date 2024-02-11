def producte(data):
    a, b = map(list, zip(*data))
    
    count_dict = {}
    for item in b:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1

    print(count_dict)

producte([('Рубашка', 'Одежда'), ('Кружка', 'Посуда')])
producte([('Рубашка', 'Одежда'), ('Штаны', 'Одежда'), ('Кружка', 'Посуда')])
producte([('Ручка', 'Канцелярия'), ('Тетрадь', 'Канцелярия'), ('Кружка', 'Посуда'), ('Стул', 'Мебель')])