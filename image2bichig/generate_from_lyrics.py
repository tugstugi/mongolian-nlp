#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Generate synthetic dataset from Mongolian song lyrics using the program 'pango-view'."""
__author__ = 'Erdene-Ochir Tuguldur'

import os
import gzip
import random


# see the fonts folder
fonts = [
    'Mongolian White',
    'Mongolian Art',
    'Mongolian Writing',
    'Mongolian Title',
    'Baga Syurga',
    'Baga Bichimel',
    'Baga Chagan',
    'Baga Garchag',
    'Baga Urga',
    'MT-Gegeen',
    'Noto Sans Mongolian'
]
font_sizes = [29, 30, 31, 32]
# some font doesn't support ᠀ variations, so make it less probable to sample from ᠀ variations
punctuations = ['᠀', '᠀᠋', '᠀᠌', '᠀᠍'] + ['᠁', '᠂', '᠃', '᠄', '᠅'] * 20
numerals = '᠐᠑᠒᠓᠔᠕᠖᠗᠘᠙'


def read_content(f='../bichig2cyrillic/lyrics.txt.gz', max_words=10):
    lines = []
    for line in gzip.open(f, 'rt').readlines():
        _, traditional_txt = line.strip().split('|')
        if len(traditional_txt.split()) <= max_words:
            lines.append(traditional_txt)
    return lines


def generate_image(text, f):
    font = random.choice(fonts)
    font_size = random.choice(font_sizes)
    cmd = "pango-view --output=%s --rotate=-90 --no-display --font='%s %i' --margin='5 0 5 0' --text \"%s\"" \
          % (f, font, font_size, text)
    os.system(cmd)


if __name__ == '__main__':
    for idx, val in enumerate(read_content()):
        # append punctuations randomly
        if random.random() < 0.05:
            punctuation = random.choice(punctuations)
            val = val + punctuation if random.choice([True, False]) else punctuation + ' ' + val

        output_file = 'images/lyrics-%i.png' % idx
        generate_image(val, output_file)
        print(output_file + '|' + val)
