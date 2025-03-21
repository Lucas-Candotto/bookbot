def get_num_words(file_contents):
    split_words = file_contents.split()
    num_of_words = len(split_words)
    return num_of_words
    

def get_characters (file_contents):
    book_text = file_contents
    lower_text = book_text.lower() 
    split_characters = list(lower_text)
    characters_dict = {}
    for char in split_characters:
        if char in characters_dict:
            characters_dict[char] += 1
        else:
            characters_dict[char] = 1
    return characters_dict

def sort_char_count(char_count):
    result = []
    for char in char_count:
        char_dict = {"char": char, "count": char_count[char]}
        result.append(char_dict)
    def get_count(item):
        return item["count"]
    
    result.sort(reverse=True, key=get_count)
    
    return result