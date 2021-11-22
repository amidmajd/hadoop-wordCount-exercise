#!/usr/bin/env python3

from itertools import groupby
from operator import itemgetter
import sys


def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.strip().split(separator, 1)


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)

    # groupby: generates a break or new group every time the value of the key function changes
    # groupby bellow returns a word as key AND all of it's Continuous separate counts as value as a list
    # so for this to work keys need to be sorted first
    # which is done automatically by hadoop's internal shuffle & sort when running mapreduce
    for current_word, word_counts_list in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in word_counts_list)
            print(current_word, total_count, sep=separator)
        except ValueError:
            # if count was not a number don't count it
            pass


if __name__ == "__main__":
    main()
