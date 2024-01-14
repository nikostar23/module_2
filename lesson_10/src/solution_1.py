def visiting_store(price: int, visiting: int):
    if 10 <= visiting < 20:
        print(int(price*90/100))
    elif visiting >= 20:
        print(int(price*80/100))
    else:
        print(price)

visiting_store(100, 5)
visiting_store(200, 10)
visiting_store(150, 20)
