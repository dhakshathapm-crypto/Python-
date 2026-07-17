def most_common_word(sentence):
    words = sentence.split()  # breaks sentence into a list of words
    counts = {}
    
    for word in words:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
    
    # find the word with the highest count
    most_common = max(counts, key=counts.get)
    return most_common, counts[most_common]

sentence = "the cat sat on the mat the cat ran"
word, count = most_common_word(sentence)
print(word, count)
