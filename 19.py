def reverse_sentence(sentence):
    words = sentence.split()
    words.reverse()
    words[0] = words[0][:-1]
    reversed_sentence = " ".join(words) + "."
    print(words)
    print(reversed_sentence)

#    print(reversed_list)
    # return reversed_sentence


if __name__ == '__main__':
    reverse_sentence('Ala ma kota.')
