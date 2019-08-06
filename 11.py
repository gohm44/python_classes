def interslave(items: list, mask: list):
    l = min(len(items), len(mask))
    list_output = []
    for e in range(l):
        if mask[e] == True:
            list_output.append(items[e])
    print(list_output)
# def get_masked(items, mask):
#     return [item for item, item_mask in zip(item, mask) if item_mask]

if __name__ == '__main__':
    interslave(items=[31, 2, 3, 4, 5, 6], mask=[True, False, True, False, True, True, False])