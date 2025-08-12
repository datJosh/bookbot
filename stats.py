def count_words(str):
    words = str.split()
    num_words = len(words)
    print(f"{num_words} words found in the document")

def count_characters(str):
    dict_chars = {}
    for s in str:
        char = s.lower()
        if char in dict_chars:
            dict_chars[char] += 1
        else:
            dict_chars[char] = 1
    print(dict_chars)