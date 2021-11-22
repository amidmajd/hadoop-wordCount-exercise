#!/usr/bin/env python3

import sys

STOP_WORDS = ['hasn', 'few', "it's", 'before', 'while', 'be', 'up', 'haven', 'with', 'm', "you'd", 'myself',
              'here', 'where', 'each', 'had', 'needn', 'but', 'no', 'won', 'him', "doesn't", 'when', 'and',
              'more', 'am', 'now', 'theirs', "weren't", 'out', 'only', 'wouldn', 'shan', "that'll", 'other',
              'they', 'wasn', 'from', 'whom', "shouldn't", "mustn't", 'on', 'about', 'in', 'ourselves',
              'once', 'then', 'her', 'at', "don't", 'most', 'what', "you'll", 'such', 'very', 'o', 'too',
              'after', 'been', "hasn't", 'don', 'ma', 'me', 'we', 'into', "haven't", 'than', "she's",
              'didn', 'd', 'themselves', 'are', 'his', 's', "shan't", 'against', 'weren', 'how', 'my',
              'doesn', 'herself', 'or', 'y', 'so', 'she', 'all', 'both', 'hadn', 'not', 'many', ''
              'couldn', 'same', 'through', "you're", 'ain', 'just', "aren't", 'off', "mightn't", 'he',
              'will', 'you', 'our', 'its', 'should', "should've", 'who', 'the', 'have', 'of', 'do',
              'these', 'until', 'above', 'was', 'doing', "needn't", 'that', 'himself', 'own', 'were',
              'for', 'further', "hadn't", 'over', 'as', "couldn't", "won't", 'an', 'which', "wouldn't",
              'is', 'nor', 'because', 'a', 'i', 'having', 'between', 'if', 'did', 'aren', 'it', 'during',
              'some', 'mightn', 'mustn', 'down', 'can', "wasn't", 're', 'there', 'isn', 'their', 'to',
              'those', 'under', 'does', 'shouldn', 'ours', 'them', 't', 'll', 'this', 'by', "isn't",
              'itself', 'why', 'below', 'again', "you've", "didn't", 'your', 'being', 'yourselves', 'yours',
              'any', 'yourself', 'has', 've', 'hers', 'us', 'would', 'may', 'maybe']


def remove_chars(string, list_of_chars):
    for char in list_of_chars:
        string = string.replace(char, "")
    return string


def clean_word(word):
    # returns cleaned word or None or empty string if input is not a propper word
    word = remove_chars(word, list("\"':;,./\\<>\{}()-–_=!#$%^&*~“”…•" + '0123456789')).lower()
    if word not in STOP_WORDS:
        return word
    else:
        return None


def read_input(file):
    for line in file:
        # split the line into words
        yield line.split()


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    for words in data:
        for word in words:
            cleaned_word = clean_word(word)
            if cleaned_word:
                print(clean_word(word), 1, sep=separator)


if __name__ == "__main__":
    main()
