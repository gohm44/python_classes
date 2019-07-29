def invert_dic(string):
    string = string.lower()
    string = string.replace(" ", "")
    histogram = {}
    # string = string.split()
    print(string)
    for k in range(len(string)):
        print(k)
        znak = string[k]
        if znak in histogram:
             histogram[string[k]] += 1
        histogram[string[k]] = 1
        print(string[k])
    print(histogram)



if __name__ == '__main__':
    invert_dic("Go Relayr!")
