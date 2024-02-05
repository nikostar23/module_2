def collect_data():                  # сбор данных
    processed_data = process_data(data)
    return processed_data


def process_data(data):      
    average = sum(data) / len(data)  # Вычисление среднего значения
    summarized_data = summarize_data(average)
    return summarized_data


def summarize_data(average):         # Создание отчета
    summary = f"Итог: Среднее значение: {average}"
    return summary

data = [1, 2, 3, 4, 5]
data = [10, 15, 5, 20]
result = collect_data()
print(result)

