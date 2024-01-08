def synonyms(words: dict):
    word = input("Введите слово: ")
    if word in words:
        print("Синоним: ", words[word])
    elif word in words.values():
        for key in list(words.keys()):
            if words[key] == word:
                print("Синоним: ", key)
    else:
        print('Нет слова в словаре. Нужно ли его добавить? (Y/N)')
        answer = input()
        if answer == "Y":
            word_new = input("Введите синоним: ")
            words.setdefault(word, word_new)
    print(words)     
    
synonyms({'Красивый': 'Прекрасный', 'Уродливый': 'Некрасивый', 'Сложный': 'Запутанный', 'Простой': 'Легкий'})