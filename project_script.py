import random

def wizard(w):
    constraints = []
    wizdict = {}
    for c in range(0, w):
        wizdict[c] = random.randint(0, 1000000)

    for key in range(0, w):
        for key2 in range(key + 1, w, 2):
            for key3 in range(key2 + 1, w, 2):
                lst = []
                lst2 = []
                if wizdict[key] not in range(wizdict[key2], wizdict[key3] + 1):
                    lst = [key2, key3, key]
                    lst2 = [key3, key2, key]
                if lst not in constraints:
                    constraints.append(lst)
                if lst2 not in constraints:
                    constraints.append(lst2)

    print(constraints)
    print(len(constraints))
