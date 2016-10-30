import os
import sys
import string
import operator

def load_data(filepath):                # функция открывает файловый поток, считывает текст, закрывает поток и возвращает текст.
    if not os.path.exists(filepath):
        return None
    file = open(filepath, "r")
    text = file.read()
    file.close()
    return text


def get_most_frequent_words(text):              # функция преобразует текст в словарь из слов в порядке убывания частоты
    table = str.maketrans("", "")
    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
    words = text.split(None)                # word - список из единичных слов

    frequencies = {}
    for word in words:
        trimmed = word.translate(remove_punctuation_map)                # удаление знаков пунктуации
        if trimmed.isalpha():
            frequencies[trimmed] = frequencies.get(trimmed, 0) + 1      # frequencies - список из слов и их количества

    return frequencies


if __name__ == '__main__':
    data_dir = input('Укажите путь до файла: ')
    text = load_data(data_dir)
    frequencies = get_most_frequent_words(text)
    keys = sorted(frequencies.items(), key=operator.itemgetter(1), reverse=True)    # список слов и их место по частоте использования
    for number in range(10):
            print ("%-32s %d" % (keys[number]))
