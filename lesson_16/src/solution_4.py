n = int(input('Введите количество полок  '))
m = input('Введите продажи по товарам  ')

m = m.split(';')
if len(m) != n:
    print('Ошибка: введено колчество продаж товаров, не соответствующее количеству полок')

a=[]

for i in range(len(m)):
    m[i] = m[i].split(',')
    a.append(m[i])

for i in range(n):
    for j in range(n):
        a[i][j] = int(a[i][j])

print('Продажи: ', a)