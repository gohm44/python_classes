def invert_map(dictionary):
    inverted_dic = {}
    for k, v in dictionary.items():
        inverted_dic['{}'.format(v)] = k
    print(inverted_dic)


if __name__ == '__main__':
    invert_map({'a': 1, 'b': 3})
