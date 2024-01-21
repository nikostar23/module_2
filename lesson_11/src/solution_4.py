def convert_units_with_while(units: list):
    units_1 = []
    units_2 = {}
    i = 0
    while i < len(units):
        units_1.append(units[i] * 3.28084)
        i = i + 1
    units_2 = dict(zip(units, units_1))
    for num, item in units_2.items():
        print(f'{num} meter (s) = {item} foot (feed)')

convert_units_with_while([1, 2])