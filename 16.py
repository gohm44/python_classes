import string

def invert_dic(stringi):
    stringi = stringi.lower()
    stringi = stringi.replace(" ", "")
    histogram = {}
    # string = string.split()
    print(stringi)
    for k in range(len(stringi)):
        znak = stringi[k]
        if znak in histogram:
             histogram[stringi[k]] += 1
        else:
            histogram[stringi[k]] = 1
    for s in len(string.ascii_lowercase)
    print(histogram)



if __name__ == '__main__':
    invert_dic("Go Relayr!")
