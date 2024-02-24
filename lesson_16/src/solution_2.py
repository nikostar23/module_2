n = int(input('Введите количество полок  '))
m = input('Введите длины полок  ')
p = input('Введите колчество товаров  ')

m = m.split(',')
for i in range(len(m)):
    m[i] = int(m[i])
if len(m) != n:
    print('Ошибка: введено количество длин полок, не соответствующее их количеству')

a = []

a = [0 for i in range(n)]

p = p.split(',')
for i in range(len(p)):
    p[i] = int(p[i])
if len(p) != n:
    print('Ошибка: введено количество товаров, не соответствующее количеству полок')

b = zip(m, a)
c = list(b)

for j in range(len(c)):
    c[j] = list(c[j])

for i in range(n):    
    c[i][1] = p[i]

print('Полки: ', c)
