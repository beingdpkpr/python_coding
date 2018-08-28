
def countEven(inputString):
    count = 1
    index = 0
    flag = False
    for i in range(1, len(inputString)):
        if inputString[i-1] == inputString[i]:
            if index is 0:
                index = i-1
            count += 1
        else:
            if count > 1 and count % 2 != 0:
                count = 1
                index = 0
            if count > 1 and count % 2 == 0:
                break
    if count % 2 == 0:
        flag = True
    else:
        flag = False
    return count, index, flag


def removeChar(inputString):
    count, index, flag = countEven(inputString)
    while flag:
        inputString = inputString[:index] + inputString[index+count:]
        count, index, flag = countEven(inputString)

    return inputString


inputString = input()
inputString = removeChar(inputString)
print(inputString)
