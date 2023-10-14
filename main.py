with open("books/frankenstein.txt") as file:
    file_content = file.read()
    word_count = len(file_content.split())
    dict_character = {}
    for word in file_content.split():
        for character in word.lower():
            try:
                dict_character[character] += 1
            except:
                dict_character[character] = 1

    list_of_character = list(dict_character.items())
    list_of_character.sort(key=lambda x: x[1], reverse=True)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for i, j in list_of_character:
        if i.isalpha():
            print(f"The '{i}' character was found {j} times")
            
    print("--- End report ---")
