def main():
    frankenstein = './books/frankenstein.txt'
    text = get_book_text(frankenstein)
    print(get_book_word_count(text))
    
def get_book_text(path):
    with open(path, "r") as f:
        return f.read()

def get_book_word_count(string):
    word_count = len(string.split())
    return f"Found {word_count} total words"

main()