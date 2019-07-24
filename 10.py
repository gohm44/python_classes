def interslave(elementy1: list, elementy2: list):
    l = min(len(elementy1), len(elementy2))
    list_output = []
    for e in range(l):
        list_output.append(elementy1[e])
        list_output.append(elementy2[e])
    print(list_output)


if __name__ == '__main__':
    interslave(elementy1=[31, 2, 3, 4, 5, 6], elementy2=[1, 42, 553, 4, 665, "f", 4])