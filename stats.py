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

def sort_book_character_count(character_count_dict):
    sorted_list = []
    for key in character_count_dict:
        value = character_count_dict[key]
        char_dict = {"char": key, "num": value}
        sorted_list.append(char_dict)
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list

def sort_on(items):
    return items["num"]