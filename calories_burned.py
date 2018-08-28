

for i in range(int(input())):
    size = int(input())
    distArray = input().split()
    distArray = list(map(int, distArray))
    sortedDistanceArray = sorted(distArray, reverse=True)
    if size == len(sortedDistanceArray):
        calArray = []
        totalDistanceCovered = 0
        todayDistanceCovered = 0
        for j in range(size):
            todayDistanceCovered = int(sortedDistanceArray[j])
            caloriesBurned = 2 * totalDistanceCovered + todayDistanceCovered
            totalDistanceCovered = totalDistanceCovered + todayDistanceCovered
            calArray.append(caloriesBurned)

        print(sum(calArray))
