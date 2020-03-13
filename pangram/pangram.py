def is_pangram(sentence):
    x = "abcdefghijklmnopqrstuvwxyz"
    for i in x:
        if i not in sentence.lower():
            return False
    return True
