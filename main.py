from sys import argv
from stats import get_book_word_count, get_book_character_count, sort_book_character_count

def main():
    if len(argv) != 2:
        raise SystemExit("Usage: python3 main.py <path_to_book>")
    path_to_book = argv[1]
    write_report(path_to_book)
    
def get_book_text(path_to_book:str) -> str:
    with open(path_to_book, "r") as f:
        return f.read()
    
def write_report(path_to_book:str) -> None:
    print("============ BOOKBOT ============")

    text = get_book_text(path_to_book)
    print(f"Analyzing book found at {path_to_book}...")

    word_count = get_book_word_count(text)
    print("----------- Word Count ----------")
    print(word_count)

    character_count = get_book_character_count(text)
    print("--------- Character Count -------")
    sorted_character_count = sort_book_character_count(character_count)
    for item in sorted_character_count:
        char, value = item["char"], item["num"]
        if not char.isalpha():
            continue
        print(f"{char}: {value}")
    
    print("============= END ===============")

main()