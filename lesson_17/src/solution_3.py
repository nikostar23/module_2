data = ['[', ']', '(', ')', '{', '}']
d = []
a = []

def bracket_balance(skob: str):
    for i in range(len(skob)):
        d.append(skob[i])
    print(d)
    
    for i in range(len(d)):
        if d[i] in data:
            a.append(list.index(data[i]))
    print(a)



bracket_balance('{([])}')