import numpy as np

model = "model.txt"
length = 1000

wordsCollection = []
with open(model, 'r') as acd:
    for line in acd:
        ab = line[:-1]
        wordsCollection.append(ab)

def pairsCreate(wordsCollection):
    for a in range(len(wordsCollection)-1):
        yield (wordsCollection[a], wordsCollection[a+1])
        
pairs = pairsCreate(wordsCollection)

worldList = {}

for wordOne, wordTwo in pairs:
    if wordOne in worldList.keys():
        worldList[wordOne].append(wordTwo)
    else:
        worldList[wordOne] = [wordTwo]

wordFirst = np.random.choice(wordsCollection)

chain = [wordFirst]

for a in range(length):
    chain.append(np.random.choice(worldList[chain[-1]]))


print(' '.join(chain))

a = input()