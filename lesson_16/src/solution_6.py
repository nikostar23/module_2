n = int(input('Введите размер рабочей зоны  '))
a = [[5 for _ in range(n)] for _ in range(n)]

for i in range(n):
    a[i][i] = 0

k = n - 1       
for i in range(0 , n // 2):
    for j in range(i + 1, k):
        a[i][j] = 1
    k -= 1

k = n - 1
t = 1       
for i in range(n - 1 , n // 2, -1):
    for j in range(t, k):
        a[i][j] = 3
    k -= 1
    t += 1

k = n - 1       
for j in range(0 , n // 2):
    for i in range(j + 1, k):
        a[i][j] = 2
    k -= 1

k = n - 1
t = 1       
for j in range(n - 1 , n // 2, -1):
    for i in range(t, k):
        a[i][j] = 4
    k -= 1
    t += 1

for row in a:
    print(' '.join([str(elem) for elem in row]))