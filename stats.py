def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_characters(book_text):
    characters = {}
    for character in book_text.lower():
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

def sort_on(characters):
    return characters["count"]

def sort_characters(characters):
    sorted_characters = []
    for character in characters:
        dictionary = {"character": character, "count": characters[character]}
        sorted_characters.append(dictionary)
    sorted_characters.sort(reverse=True, key=sort_on)
    return sorted_characters