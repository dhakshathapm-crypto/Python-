def count_letters(word):
    counts = {}
    for letter in word:
        if letter in counts:
            counts[letter] = counts[letter] + 1
        else:
            counts[letter] = 1
    return counts

def is_anagram(word1, word2):
    return count_letters(word1) == count_letters(word2)

print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False
