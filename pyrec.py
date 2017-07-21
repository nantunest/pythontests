tree = {
    "n1": [1,11],
    "n2": [4,5,6],
    "n3": [7,9],
    "n4": [88,99]
}


def comblist(t):

    result = []
    
    # pop item
    i = t.popitem()

    # if leaf return list with elements
    if len(t) == 0:
        result = [[e] for e in i[1]]
    
    else:
        # for each element in the tree level
        for e in i[1]:
            # fetch combination from elements below
            presult = comblist(t)
            
            # add elements from this level to the result
            for r in presult:
                result.append([e]+r)
         
    # push item back
    t[i[0]] = i[1]

    return result

r = comblist(tree)

print r
