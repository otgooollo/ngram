wordstring = 'it was the best of times it was the worst of times '
wordstring += 'it was the age of wisdom it was the age of foolishness'
wordlist = wordstring.split()
print(wordlist[0:1])
print(wordlist[0:2])
print(wordlist[0:4])
print(wordlist[0:6])

print('---------------------------------------------------------------')
i = 0
for items in wordlist:
    print(wordlist[i: i+5])
    i += 1
print('---------------------------------------------------------------')
    
def getNGrams(wordlist, n):
    return [wordlist[i:i+n] for i in range(len(wordlist)-(n-1))]

def getNGrams(wordlist, n):
    ngrams = []
    for i in range(len(wordlist)-(n-1)):
        ngrams.append(wordlist[i:i+n])
    return ngrams

wordstring = 'it was the best of times it was the worst of times '
wordstring += 'it was the age of wisdom it was the age of foolishness'
allMyWords = wordstring.split()

print(getNGrams(allMyWords, 5))

test1 = 'here are four words'
test2 = 'this test sentence has eight words in it'
print('---------------------------------------------------------------')
print(getNGrams(test1.split(), 3))
print('---------------------------------------------------------------')
print(getNGrams(test2.split(), 5))
