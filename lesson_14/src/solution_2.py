def price_list(lst):
    lst_1 = list(map(
    lambda num: round(lst[num] /100) * 100, range(0, len(lst))))
    
    lst_2 = set(lst_1)
    
    print(sorted(lst_2))

price_list([99, 150, 200, 349, 501])
price_list([80, 70, 270, 170, 310])