def num_items(num: list) -> None:
    k = num[1]
    n = num[0]
    m = num[-1]
    print("Числа подсписка: ", num[n:m:k])

num_items([1, 2, 3, 4, 5])
num_items([2, 1, 6])
