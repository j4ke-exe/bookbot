def get_num_words(text):
    return len(text.split())

def get_char_counts(text):
    counts = {}
    for char in text:
        char = char.lower()
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_char_counts(char_dict):
    sorted_list = []
    for char, count in char_dict.items():
        sorted_list.append({"char": char, "count": count})
    sorted_list.sort(reverse=True, key=lambda x: x["count"])
    return sorted_list