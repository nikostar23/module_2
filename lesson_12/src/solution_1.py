def collect_data(data):
    return data

def process_data(data):
    midle = sum(data) / len(data)
    return midle

def summarize_data(midle):
    print(f'Итог: Среднее значение: {midle}')

data_1 = collect_data([1, 2, 3, 4, 5])
data_1 = collect_data([10, 15, 5, 20])
midle = process_data(data_1)
summarize_data(midle)

#from typing import Callable

#def process_data(func: Callable[[list], int], x = sum(data) / int(len(data))):
 #   return func(x)

