import random

def shake_word(word):
    if len(word) <= 3: return word

    middle = list(word[1:-1])
    random.shuffle(middle)

    return word[0] + ''.join(middle) + word[-1]

def shake_text(text):
    return ' '.join(shake_word(word) for word in text.split())
