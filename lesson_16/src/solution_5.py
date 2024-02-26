n = int(input('Введите ширину матрицы  '))
a = [[0 for _ in range(n)] for _ in range(n)]

row_start = 0
row_end = n - 1
col_start = 0
col_end = n - 1
current_num = 1

while row_start <= row_end and col_start <= col_end:
    # Заполнение верхней строки
    for j in range(col_start, col_end + 1):
        a[row_start][j] = current_num
        current_num += 1
    row_start += 1

    # Заполнение последнего столбца
    for i in range(row_start, row_end + 1):
        a[i][col_end] = current_num
        current_num += 1
    col_end -= 1

    # Заполнение нижней строки
    if row_start <= row_end:  # Проверка, что остается несколько строк
        for j in range(col_end, col_start - 1, -1):
            a[row_end][j] = current_num
            current_num += 1
        row_end -= 1

    # Заполнение первого столбца
    if col_start <= col_end:  # Проверка, что остается несколько столбцов
        for i in range(row_end, row_start - 1, -1):
            a[i][col_start] = current_num
            current_num += 1
        col_start += 1

#for row in a:
#    print('\t'.join(map(str, row)))

k = len(str(n ^ 2)) + 2  # Находим самый длинный элемент в матрице
for row in a:
    format_row = [str(num).rjust(k) for num in row]
    print(" ".join(format_row))
