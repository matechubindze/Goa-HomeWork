def insert_word(sentence, word, index):
    words = sentence.split()
    words.insert(index, word)
    return " ".join(words)

print(insert_word("I love programming", "Python", 2))
