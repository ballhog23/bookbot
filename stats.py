from typing import TypedDict, Dict, List

class CharacterDict(TypedDict):
    char: str
    num: int

def get_book_word_count(string: str) -> str:
    word_count = len(string.split())
    return f"Found {word_count} total words"

def get_book_character_count(string: str) -> Dict[str, int]:
    character_count: Dict[str, int] = {}
    for char in string.lower():
        if char not in character_count:
            character_count[char] = 1
        else:
            character_count[char] +=1
    return character_count

def sort_book_character_count(character_count_dict: Dict[str, int]) -> List[CharacterDict]:
    sorted_list = []
    for key in character_count_dict:
        value = character_count_dict[key]
        char_dict = {"char": key, "num": value}
        sorted_list.append(char_dict)
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list

def sort_on(items: CharacterDict) -> int:
    return items["num"]