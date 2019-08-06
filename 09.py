def kth_elements(elementy: list, k: int):
    return elementy[k-1::k]
# islice

if __name__ == '__main__':
    kth_elements(elementy=[31, 2, 3, 4, 5, 6], k=2)
