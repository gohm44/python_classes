def find_missing(source, target):
    missing = []
    """Napisz funkcję find_missing(source, target) zwracającą (w dowolnej
formie) wszystkie elementy z listy source, które nie znajdują się na liście
target. Każdy taki element powinien zostać zwrócony tylko raz. Przykładowo, dla list [1, 2, 3, 2] i [1, 3] zwracana kolekcja powinna zawierać
jeden element 2"""
    for e in source:
        if e not in target and e not in missing:
            missing.append(e)

    print(missing)



if __name__ == '__main__':
    find_missing([1,2,3,2,6], [1,3])
