import math


def read_words(filename):
    f = open(filename)
    d = {}
    count = 0
    for line in f:
        words = line.lower().split()
        for word in words:
            if word.isalpha():
                if word in d:
                    d[word] = d[word]+1
                else:
                    d[word] = 1
                count += 1

    f.close()
    for word in d:
        d[word] = d[word]/count
    return d


def edit1(word):
    n = len(word)
    variations = set()
    letters = "abcdefghijklmnopqrstuvwxyz"

    # deletions
    for i in range(n):
        newword = word[:i]+word[i+1:]
        variations.add(newword)

    # replacements
    for i in range(n):
        for c in letters:
            if word[i] != c:
                newword = word[:i]+c+word[i+1:]
                variations.add(newword)

    # insertions
    for i in range(n+1):
        for c in letters:
            newword = word[:i]+c+word[i:]
            variations.add(newword)

    # inversions
    for i in range(n-1):
        for c in letters:
            if word[i] != word[i+1]:
                newword = word[:i]+word[i+1]+word[i]+word[i+2:]
                variations.add(newword)

    return variations


def edit_k(word, k):
    variations = {word}
    for i in range(k):
        newvariations = set()
        for v in variations:
            newvariations |= edit1(v)
        variations = newvariations
    return variations

# word=input('Enter the word: ')


def error_probability(e, n, q):
    binc = math.comb(n, e)
    return binc*(q**e)*(1-q)**(n-e)


def correct_word(word, maxErrors, q, p_c, top):
    canddates = []
    for e in range(maxErrors+1):
        variations = edit_k(word, e)
        for c in variations:
            if c in p_c:
                p_wc = error_probability(e, len(c), q)
                score = p_c[c]*p_wc
                canddates.append((score, c))
    canddates.sort(reverse=True)
    return canddates[:top]


word = input("insert a word")
p_c = read_words("big.txt")
corrections = correct_word(word, 3, 0.01, p_c, 5)
print(corrections)
