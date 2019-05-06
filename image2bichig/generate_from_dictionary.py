#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Generate synthetic dataset from a dictionary file training images using the program 'pango-view'."""
__author__ = 'Erdene-Ochir Tuguldur'

import gzip
import random

from generate_from_lyrics import generate_image


def generate_random_text(words, min_word_count=3, max_word_count=8):
    word_count = random.randint(min_word_count, max_word_count)
    word_indices = random.sample(range(len(words)), word_count)
    return " ".join([words[i] for i in word_indices])


if __name__ == '__main__':
    lines = gzip.open('mn_dict.txt.gz', 'rt').readlines()
    words = [l.strip() for l in lines]
    N = 10000
    for i in range(N):
        text = generate_random_text(words)
        output_file = 'images/dict-%i.png' % i
        generate_image(text, output_file)
        print("%s|%s" % (output_file, text))
