

if __name__ == '__main__':
    for i in range(0, int(input())):
        numOfTweets = int(input())
        tweetCount = {}
        for j in range(0, numOfTweets):
            data = input()
            username, tweetId = data.split()

            tweetCount[username] = tweetCount.get(username, 0) + 1

        for key, value in tweetCount.items():
            if value > 1:
                print(key, value)

