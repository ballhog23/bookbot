def main():
    frankenstein = './books/frankenstein.txt'
    text = get_book_text(frankenstein)
    print(text)
    
def get_book_text(path):
    with open(path, "r") as f:
        return f.read()

main()