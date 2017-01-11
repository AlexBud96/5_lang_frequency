import re
import os
from collections import Counter


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file:
        return file.read().lower()


def lang_frequency(text):
    words = re.findall(r'\w+', text)
    most_common_words = 10
    return Counter(words).most_common(most_common_words)


if __name__ == '__main__':
    filepath = input('Введите путь до файла: ')
    text = load_data(filepath)
    if not text:
        print('Не удалось открыть файл')
    else:
        for word, frequency in lang_frequency(text):
            print(word, frequency)
