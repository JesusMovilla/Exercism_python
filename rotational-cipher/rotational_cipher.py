from string import ascii_lowercase as low_case
from string import ascii_uppercase as up_case


def rotate(text, key):
    lookup = str.maketrans(low_case + up_case, low_case[key:] +
                           low_case[:key] + up_case[key:] + up_case[:key])
    return text.translate(lookup)
