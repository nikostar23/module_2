def price_list(lst):
    lst_1 = list(filter(
    lambda num: lst[num] //100, range(0, len(lst))))
    
    lst_2 = []
    for i in lst_1:
        lst_2.append(lst[i] // 100 * 100)
    
    print(lst_2)

price_list([99, 150, 200, 349, 501])