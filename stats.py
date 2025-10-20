def get_number_of_words(text):
    words = text.split()
    return len(words)

def number_of_each_character(text):
    char_count = {}
    for char in text:
        if char.lower() in char_count:
            char_count[char.lower()] += 1 # Normalize to lowercase and add to count
        else:
            char_count[char.lower()] = 1 # Initialize count
    return char_count

def sorted_character_count(char_count):
    result = [{"char": char, "num": count} for char, count in char_count.items()]
    result.sort(key=lambda x: x["char"])
    return result