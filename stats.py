
def get_num_words(text):
    words = text.split()

    return len(words)

def get_char_dict(text):
    char_set = set()
    text = text.lower()
    char_dict = {}

    for char in text:
        if char not in char_set:
            char_set.add(char)
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_char_dict(char_dict):
    char_dict_list = []

    for key in char_dict:
        char_dict_list.append({"char" : key, "num" : char_dict[key] })

    char_dict_list.sort(reverse=True, key=sort_on)

    return char_dict_list
