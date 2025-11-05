from stats import get_book_word_count, get_book_character_count
def main():
    frankenstein = './books/frankenstein.txt'
    text = get_book_text(frankenstein)
    word_count = get_book_word_count(text)
    character_count = get_book_character_count(text)
    
def get_book_text(path):
    with open(path, "r") as f:
        return f.read()

main()