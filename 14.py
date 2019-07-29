def invert_dic(dictionary):
    inverted_dic = {}
    prev_k = ""
    prev_v = list(dictionary.values())[0]
    first = True
    for k, v in dictionary.items():
        if first:
            inverted_dic[f'{v}'] = k
            first = False
        if v == prev_v and not first:
            inverted_dic[f'{v}'] = list(prev_k)
            inverted_dic[f'{v}'].append(k)
        else:
            inverted_dic[f'{v}'] = k
        prev_k = k
        prev_v = v
    print(inverted_dic)


if __name__ == '__main__':
    invert_dic({'a': 1, 'b': 3, 'c': 3, 'd': 5})
