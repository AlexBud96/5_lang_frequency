import os
import sys
import string
import operator

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    file = open(filepath, "r")
    text = file.read()
    file.close()
    return text


def get_most_frequent_words(text):
    table = str.maketrans("", "")
    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
    words = text.lower().split(None)

    frequencies = {}
    for word in words:
        trimmed = word.translate(remove_punctuation_map)
        if trimmed.isalpha():
            frequencies[trimmed] = frequencies.get(trimmed, 0) + 1

    return frequencies


if __name__ == '__main__':
    data_dir = input('Укажите путь до файла: ')
    text = load_data(data_dir)
    frequencies = get_most_frequent_words(text)
    keys = sorted(frequencies.items(), key=operator.itemgetter(1), reverse=True)
    for number in range(10):
            print ("%-32s %d" % (keys[number]))
