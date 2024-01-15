def calculate_discount(cost, index = 0, first_cost = None):
    cost_1 = []
    
    if index < len(cost):
        next_cost = cost[index]
        cost_discount = first_cost * 0.1 if first_cost is not None else 0
        new_cost = int(next_cost - cost_discount if first_cost is not None else next_cost)
        cost_1.append(new_cost)
        cost_1 += calculate_discount(cost, index + 1, next_cost)
    return cost_1

cost = [1000, 2000, 3000]
cost = [5000, 10000, 15000]
cost = [100, 200, 300, 400]
cost = [50, 100]
result = calculate_discount(cost)
print("Выходные данные:", '. '.join(result))

# это можно сделать в цикле
#def calculate_discount(cost):
#    cost_1 = []
#    cost_1.append(cost[0])
   
#    for i in range(1, len(cost)):
#        cost_1.append(int(cost[i] - cost[i-1] * 10  / 100))
#    print(cost_1)

