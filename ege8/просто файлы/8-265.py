from itertools import permutations

A = "СПОРТЛОТО"
allWords = [ "".join(w) for w in set( permutations(A)) ]
print(allWords)
allWords = [ w for w in allWords if w[0] != 'О' and w[-1] != 'О']

print( len(allWords) )

