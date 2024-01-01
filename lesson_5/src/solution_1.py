def swap_parts(word: str) -> None:
    index_of_middle = len(word) // 2
    print(word[index_of_middle:] + word[:index_of_middle])
    
    
swap_parts("Logomachine")
swap_parts("ArtSpace")
swap_parts("Designify")
