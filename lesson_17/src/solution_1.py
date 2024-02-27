def find_element(data: list, num):
    k = 0
    for i in range(len(data)):
        if num == data[i]:
            k += 1
    print(k != 0)


#def find_element(data: list, num) -> bool:
#    for i in range(len(data)):
#        if num in data:
#           return True
#        else:
#            return False

find_element([1, 3, 5], 6)
find_element(['tree', 'red', 'yellow'], 'red')
