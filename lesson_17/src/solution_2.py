def binary_find_element(data: list, num):
    a = data[0]
    b = data[-1]
    c = len(data) // 2
    
    if num == data[c]:
        print(True)
    if num < data[c]:
        for _ in range(c):
            c = c // 2
        if num == data[c]:
            print(True)
    if num > data[c]:
        for _ in range(c, len(data)):
            c = (len(data) + c) // 2
            if num == data[c]:
                print(True)
    else:
        print(False)

binary_find_element([1, 4, 6, 7, 8], 6)
