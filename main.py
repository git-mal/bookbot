def main():
    
    book_path = "books/frankenstein.txt"
    
    book_text = get_text(book_path)
    
    word_count = word_counter(book_text)

    character_count = character_counter(book_text)
    
    character_list_sorted = split_sort(character_count)

    report_formatter(book_path,word_count,character_list_sorted)

    
    



def get_text(book_path):
     with open(book_path) as f:
        return f.read()
       
def word_counter(book_text):
    text = book_text.split()
    return len(text)

def character_counter(book_text):
    counter = {}
    for i in book_text.lower():
        if i in counter:
            counter[i] += 1
        else:
            counter.update({i:1})
    
    return counter

def split_sort(character_count):
    
    def sort_on(dict):
        return dict["num"]
    
    
    character_lists = []

    for character, count in character_count.items():
        if character.isalpha() == True:
            character_lists.append({"name":character,"num":count})
        else:
            continue

    character_lists.sort(reverse=True, key=sort_on)

    return character_lists

def report_formatter(book_path,word_count,character_list_sorted):
    
    print(f"--- Begin report of {book_path} ---\n")
    print(f"{word_count} words found in this document\n")

    for char in character_list_sorted:
        print(f"the '{char["name"]}' character appeared {char["num"]} times")

    print("\n--- End of report ---")
    



if __name__=="__main__":
    main()

