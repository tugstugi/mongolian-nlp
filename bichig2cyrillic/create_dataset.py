#!/usr/bin/env python3 -u

import os
import gzip
import random

lines = gzip.open('lyrics.txt.gz', 'rt', encoding='utf-8').readlines()
lines = [line.rstrip('\n') for line in lines]
random.seed(1234)
random.shuffle(lines)

col1_lines = []
col2_lines = []
for line in lines:
    col1, col2 = line.split('|')
    col1_lines.append(col1)
    col2_lines.append(col2)


print("total: %i" % len(col1_lines))


def convert_bichig(line):
    # dataset contains sometimes '=' for '-гүйсэн' suffix, replace it with 0x202f
    line = line.replace('=', chr(0x202f))
    # replace 0x202f with '_'
    line = line.replace(chr(0x202f), '_')
    # replace whitespace with '#'
    line = line.replace(' ', '#')

    return ' '.join(line)


def convert_cyrillic(line):
    # replace whitespace with '#'
    return ' '.join(line.replace(' ', '#'))


os.makedirs('dataset', exist_ok=True)
with open('dataset/train.cyrillic', 'w') as f:
    lines = [convert_cyrillic(line) for line in col1_lines[:-6000]]
    f.write('\n'.join(lines) + '\n')
with open('dataset/train.bichig', 'w') as f:
    lines = [convert_bichig(line) for line in col2_lines[:-6000]]
    f.write('\n'.join(lines) + '\n')
with open('dataset/valid.cyrillic', 'w') as f:
    lines = [convert_cyrillic(line) for line in col1_lines[-6000:-1000]]
    f.write('\n'.join(lines) + '\n')
with open('dataset/valid.bichig', 'w') as f:
    lines = [convert_bichig(line) for line in col2_lines[-6000:-1000]]
    f.write('\n'.join(lines) + '\n')
with open('dataset/test.cyrillic', 'w') as f:
    lines = [convert_cyrillic(line) for line in col1_lines[-1000:]]
    f.write('\n'.join(lines) + '\n')
with open('dataset/test.bichig', 'w') as f:
    lines = [convert_bichig(line) for line in col2_lines[-1000:]]
    f.write('\n'.join(lines) + '\n')
