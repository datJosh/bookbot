def count_words(str):
    words = str.split()
    num_words = len(words)
    print(f"Found {num_words} total words")

def count_characters(str):
    dict_chars = {}
    for s in str:
        char = s.lower()
        if char in dict_chars:
            dict_chars[char] += 1
        else:
            dict_chars[char] = 1
    return dict_chars

def sort_characters(dict):
    list = []
    for key in dict:
        list.append({"char": key, "num": dict[key]})
    list.sort(reverse=True, key=lambda item: item["num"])
    return list