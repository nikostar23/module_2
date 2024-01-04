def text_1(text: str) -> None:
    text_2 = text.split( )
    text_3 = []
    for text in text_2:
        text_3.append(text[::-1])
    print(" ".join(text_3))


text_1('Hello World')

text_1('Python')
