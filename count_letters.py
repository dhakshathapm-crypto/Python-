def count_letters(word):
    counts = {}
    for letter in word:
        if letter in counts:
            counts[letter] = counts[letter] + 1
        else:
            counts[letter] = 1
    return counts

word = "banana"
print(count_letters(word))
