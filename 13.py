def invert_dic(dictionary):
    inverted_dic = {}
    for k, v in dictionary.items():
        inverted_dic[f'{v}'] = k
    print(inverted_dic)


if __name__ == '__main__':
    invert_dic({'a': 1, 'b': 3})
