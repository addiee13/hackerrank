import string
def alphabet_position(text):
    position = ""
    alphabet = list(string.ascii_lowercase)
    for i, char in enumerate(text):
        if char.lower() in alphabet:
            position += str(alphabet.index(char.lower()) + 1) + " "
        else:
            i += 1
    return position.strip()

print(alphabet_position("The sunset sets at twelve o' clock."))

