def is_isogram(text):
    text = text.replace(" ", "")
    print(text)
    text = text.lower()
    print(text)
    for char in text:
        if text.count(char) > 1:
            is_isogram_bool = False
            break
        else:
            is_isogram_bool = True

    print(is_isogram_bool)


if __name__ == '__main__':
    is_isogram("The dwarf only jumps")
