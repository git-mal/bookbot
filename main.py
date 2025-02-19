def main():
    
    book_path = "books/frankenstein.txt"
    
    book_text = get_text(book_path)
    
    word_count = get_count(book_text)
    
    print(word_count)


def get_text(book_path):
     with open(book_path) as f:
        return f.read()
       
def get_count(book_text):
    text = book_text.split()
    return len(text)

if __name__=="__main__":
    main()

