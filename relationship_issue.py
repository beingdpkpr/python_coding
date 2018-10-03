
def isReflexive(n, relation):
    for i in range(1, n+1):
        reflexivePair = {i: i}
        if relation.__contains__(reflexivePair) is False:
            return False
    return True

def isSymmtric(relation):
    for item in relation:
        for key, value in item.items():
            if relation.__contains__({value: key}) is False:
                return False
    return True

def isTransitive(relation):
    for i in range(0, len(relation)):
        for key1, value1 in relation[i].items():
            for j in range(i, len(relation)):
                for key2, value2 in relation[j].items():
                    if value1 == key2:
                        if relation.__contains__({key1: value2}) is False:
                            return False
                        else:
                            key1, key2, value1, value2 = 0, 0, 0, 0
    return True

# main
if __name__ == '__main__':
    for i in range(0, int(input())):
        relation = []
        test = input()
        testlist = test.split()
        if len(testlist) == 2:
            n, m = testlist[0], testlist[1]
            for i in range(0, int(m)):
                t = input().split()
                pair = {int(t[0]): int(t[1])}
                relation.append(pair)

            isSymmtric(relation)
            if isReflexive(int(n), relation) is False:
                print('NO')
            else:
                if isSymmtric(relation) is False:
                    print('NO')
                else:
                    if isTransitive(relation) is False:
                        print('NO')
                    else:
                        print('YES')



