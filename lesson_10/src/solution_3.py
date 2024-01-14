def responsible_worker(res_workers: dict):
    maxx = max(list(res_workers.values()))
    d_1 = [name for name, value in res_workers.items() if value == maxx]
    return d_1

d_1 = responsible_worker({'Анна' : 5, 'Боб' : 7, 'Сьюзен' : 9})
d_1 = responsible_worker({'Джон' : 1, 'Майкл' : 1, 'Эмили' : 1})

result = ', '.join(d_1)

print("Самый ответственный сотрудник: ", result)