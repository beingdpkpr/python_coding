def number_of_binary_trees(n: int):
    count = [0 for i in range(n + 1)]
    count[0] = count[1] = 1

    for i in range(2, n + 1):
        for j in range(i):
            count[i] += count[j] * count[i - j - 1]

    return count.pop()

# main
if __name__ == "__main__":
    for i in range(0, int(input())):
        n = int(input())
        result = number_of_binary_trees(n)
        print(result)
