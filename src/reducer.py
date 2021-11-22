#!/usr/bin/env python3

from itertools import groupby
from operator import itemgetter
import sys
import collections


counter = collections.Counter()


def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.strip().split(separator, 1)


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)

    for word, count in data:
        try:
            counter[word] += int(count)
        except ValueError:
            pass
    for word, count in counter.most_common():
        print(word, count, sep=separator)


if __name__ == "__main__":
    main()
