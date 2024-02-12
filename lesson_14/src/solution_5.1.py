from collections import Counter

def producte(data):
    a, b = map(list, zip(*data))
    
    cnt = Counter(b)
    dict(cnt)

    print(dict(cnt))

producte([('Рубашка', 'Одежда'), ('Кружка', 'Посуда')])
producte([('Рубашка', 'Одежда'), ('Штаны', 'Одежда'), ('Кружка', 'Посуда')])
producte([('Ручка', 'Канцелярия'), ('Тетрадь', 'Канцелярия'), ('Кружка', 'Посуда'), ('Стул', 'Мебель')])