

if __name__ == '__main__':
    for i in range(0, int(input())):
        numberOfDays = int(input())
        chocolateCollected = input().split()
        scaredQuotient = []
        if len(chocolateCollected) == numberOfDays:
            for i in range(0, len(chocolateCollected)):
                if i is 0:
                    scaredQuotient.append(1)
                else:
                    count = 0
                    j = i
                    flag = True
                    while j > -1 and flag:
                        if int(chocolateCollected[j]) <= int(chocolateCollected[i]):
                            count = count + 1
                            j = j - 1
                        else:
                            flag = False
                            break
                    scaredQuotient.append(count)
            print(*scaredQuotient)

