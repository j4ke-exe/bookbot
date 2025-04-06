def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_char_count(char_dict):
    sorted_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            sorted_list.append({'char': char, 'count': count})
    sorted_list.sort(key=lambda x: x['count'], reverse=True)
    return sorted_list