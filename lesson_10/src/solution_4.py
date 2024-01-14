def choose_ad_platform(budget: int):
    if budget <=1000:
        print('Google')
    elif 1000 < budget <=5000:
        print('Facebook')
    else:
        print('Instagramm')

choose_ad_platform(500)
choose_ad_platform(3000)
choose_ad_platform(6000)
