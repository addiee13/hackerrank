def spin_words(sentence):
    words = sentence.split()
    reversed_sentence = ""
    for word in words:
        if len(word) >= 5:
            reversed_word = ""
            for i in range(len(word) - 1, -1, -1):
                reversed_word += word[i]
            reversed_sentence += reversed_word + " "
        else:
            reversed_sentence += word + " "
    return reversed_sentence.strip()
print(spin_words("Hello World"))

