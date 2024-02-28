def find_element(data: list, num) -> bool:
    k = 0
    for i in range(len(data)):
        if num == data[i]:
            k += 1
    return k != 0


#def find_element(data: list, num) -> bool:
#    for i in range(len(data)):
#        if num in data:
#           return True
#        else:
#            return False

print(find_element([1, 3, 5], 6))
print(find_element(['tree', 'red', 'yellow'], 'red'))
