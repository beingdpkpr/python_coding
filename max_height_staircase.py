

for i in range(0, int(input())):
    n = int(input())
    staircase = 0
    i = 1
    while n > 0:
        n = n - i
        i = i + 1
        if n >= 0:
            staircase = staircase + 1

    print(staircase)

