def get_book_word_count(string):
    word_count = len(string.split())
    return f"Found {word_count} total words"

def get_book_character_count(string):
    character_count = {}
    lowered_string = string.lower()
    for char in lowered_string:
        if char not in character_count:
            character_count[char] = 1
        else:
            character_count[char] +=1
    return character_count