n = int(input('Введите количество полок  '))
m = input('Введите длины полок  ')

m = m.split(',')
for i in range(len(m)):
    m[i] = int(m[i])
if len(m) != n:
    print('Ошибка: введено колчество длин полок, не соответствующее их количеству')
a = []

a = [0 for i in range(n)]
b = zip(m, a)
c = list(b)

for j in range(len(c)):
    c[j] = list(c[j])

print('Полки: ', c)
