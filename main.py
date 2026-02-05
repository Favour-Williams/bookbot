import sys

from stats import countWord, countChar, sort

def main():
    print(sys.argv)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    count = countWord(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")


    print(f"Found {count} total words")

    print("--------- Character Count -------")
    char_count = sort(countChar(book_text))
    for item in char_count:
        char = item["char"]
        num = item["num"]
        print(f"{char}: {num}") 
    print("============= END ===============")


def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents



main()
