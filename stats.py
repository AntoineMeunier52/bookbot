def count_words (content):
    words = content.split()
    return len(words)

def count_char (content):
    chars = {}

    for char in content:
        char_lower = char.lower()

        if char_lower in chars:
            chars[char_lower] += 1
        else:
            chars[char_lower] = 1

    return chars

def sort_on(dict):
    return dict["count"]

def sort_chars (chars):
    res_list = []
    i = 0

    # sorted_list = []
    # for ch in num_chars_dict:
    #     sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    # sorted_list.sort(reverse=True, key=sort_on)

    for char, count in chars.items():
        res_list.append({"char": char, "count": count})
        i += 1

    res_list.sort(key=sort_on, reverse=True)
    return res_list