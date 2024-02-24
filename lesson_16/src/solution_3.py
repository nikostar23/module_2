def shelf(data):
    a = []
    n = len(data)
    for i in range(n):
        a.append(data[i][1] * (i + 1))
    
    b = []
   
    for i in range(n):
        b.append([0]*data[i][1])
        
    for i in range(n):
        for m in range(len(b[i])):
            b[i][m] = a[i]

    print('Скидки: ', b)

shelf([[4, 2], [5, 3], [6, 5]])
shelf([[3, 1], [4, 4]])
