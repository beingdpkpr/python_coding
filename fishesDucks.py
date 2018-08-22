
t = int(input())
for x in range(t):
    noOfDucks = int(input())
    ages = input().split()
    if noOfDucks == len(ages):
        if noOfDucks == 1:
            print(1)
        elif noOfDucks == 2:
            if int(ages[0]) > int(ages[1]):
                print(2, 1)
            else:
                print(1, 2)
        else:
            feeds = []
            feed = 0
            firstSame = False
            if int(ages[0]) > int(ages[1]):
                feed = 2
            else:
                feed = 1
            feeds.append(feed)
            for i in range(1, len(ages)):
                if int(ages[i]) < int(ages[i - 1]):
                    firstSame = False
                    feed = 1
                elif int(ages[i]) == int(ages[i - 1]):
                    if firstSame:
                        feed = feed + 1
                        firstSame = False
                    else:
                        feed = feed - 1
                        firstSame = True
                elif int(ages[i]) > int(ages[i - 1]) and int(ages[i]) > int(ages[i + 1]) > int(ages[i - 1]):
                    firstSame = False
                    feed = feed + 2
                else:
                    firstSame = False
                    feed = feed + 1
                feeds.append(feed)
            print(*feeds)

