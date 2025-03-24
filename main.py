import sys
from stats import count_words
from stats import count_characters
from stats import sort_characters

def get_book_text(book_path):
    with open(book_path) as book:
        book_contents = book.read()
    return book_contents

def main():
    try:
        book_text = get_book_text(sys.argv[1])
        num_words = count_words(book_text)
        characters = count_characters(book_text)
        sorted_characters = sort_characters(characters)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for item in sorted_characters:
            if item["character"].isalpha():
                print(f"{item['character']}: {item['count']}")
        print("============= END ===============")
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
main()