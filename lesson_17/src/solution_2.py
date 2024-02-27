def binary_find_element(data: list, num) -> bool:
    low = 0
    high = len(data) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if data[mid] == num:
            return True
        elif data[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
    
    return False

print(binary_find_element([1, 4, 6, 7, 8], 8))
print(binary_find_element([1, 3, 4, 6, 7, 8], 8))
print(binary_find_element([], 8))