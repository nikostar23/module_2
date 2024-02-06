def collect_data():                  # сбор данных
    return process_data(data)
    
import statistics

def process_data(data):      
    average = statistics.mean(data)  # Вычисление среднего значения
    return summarize_data(average)

def summarize_data(average):         # Создание отчета
    return f"Итог: Среднее значение: {average}"

data = [1, 2, 3, 4, 5]
data = [10, 15, 5, 20]
result = collect_data()
print(result)

