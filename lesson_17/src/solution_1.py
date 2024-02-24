def find_element(data: list, num):
    for i in range(len(data)):
        if data[i] == num:
            print(True)
        else:
            print(False)

find_element([1, 3, 5], 5)
find_element(['tree', 'red', 'yellow'], 'red')
