from itertools import permutations

str = 'eee'
perm = [''.join(p) for p in permutations(str)]
test = [p for p in permutations(str)]
print(perm)

