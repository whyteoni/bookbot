from stats import get_word_count, get_char_count, get_sorted_char_count
import sys

def get_book_text(path:str) -> str:
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()
 
def main():
    print("==== BOOKBOT LIVES! ========")
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print(f"Analyzing book at {book_path}")
    book_text = get_book_text(book_path)
    print("---- Word Count ------------")
    book_word_count = get_word_count(book_text)
    print(f"Found {book_word_count} total words")
    print("---- Character Count -------")
    book_char_count = get_char_count(book_text)
    book_sorted_char_count = get_sorted_char_count(book_char_count)

    for count in book_sorted_char_count:
        if count["name"].isalpha():
            print(f"{count['name']}: {count['num']}")
    print("===== END ==================")

main()
