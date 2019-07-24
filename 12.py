def napis():
    word = input("Type word: ")
    # proscizna
    print(word[::-1])

    #nie wiem o co kaman
    reversed_word = ''
    for d in word:
        reversed_word = d + reversed_word
    print(reversed_word)

    reversed_word = ''
    l = len(word) - 1
    while l >= 0:
        reversed_word = reversed_word + word[l]
        l = l - 1
    print(reversed_word)


if __name__ == '__main__':
    napis()