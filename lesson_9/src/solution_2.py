def convert_to_hex(items: tuple[int]):
    a = len(items)
    b = []
    for i in range(a):
        b.append((hex(items[i])))
    c = "".join(b)
    
    c = c.replace('x', '')
    c = c.replace('0', '', 1)
    print('HEX: #', c)

convert_to_hex((255, 0, 0))
convert_to_hex((0, 255, 0))
convert_to_hex((0, 0, 255))
