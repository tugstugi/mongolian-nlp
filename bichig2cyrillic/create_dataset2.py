#!/usr/bin/env python3 -u
"""Create additional training data using family and clan names from http://opendata.burtgel.gov.mn"""

import os
import gzip
import random


lines = gzip.open('../datasets/mongolian_clan_names.csv.gz', 'rt', encoding='utf-8').readlines()
lines += gzip.open('../datasets/mongolian_personal_names.csv.gz', 'rt', encoding='utf-8').readlines()
lines = [line.rstrip('\n') for line in lines]
random.seed(1234)
random.shuffle(lines)

name1_lines = []
name2_lines = []
for line in lines:
    name1, name2, _ = line.split(',')
    name1, name2 = name1.strip(), name2.strip()
    if len(name1) < 3 or len(name2) < 3:
        continue
    name1_lines.append(name1)
    name2_lines.append(name2)


misc_alphabet = 'abcdefghijklmnopqrstuvwxyz' + 'abcdefghijklmnopqrstuvwxyz'.upper()
misc_alphabet += '0123456789()[]<>-;\'"+*§$₮€%&@/\\='  # '_#' are used somewhere

col1_lines = []
col2_lines = []
for i in range(len(name1_lines)//8):
    sep1, sep2 = random.choice([[':', ' ᠄ '], [',', ' ᠂ ']])
    end1, end2 = random.choice([['.', ' ᠃'], ['!', '!'], ['?', '?']])
    col1 = (sep1+' ').join(name1_lines[8*i:8*(i+1)]) + end1
    col2 = sep2.join(name2_lines[8 * i:8 * (i + 1)]) + end2

    if random.random() < 0.05:
        misc = "".join(random.choices(list(misc_alphabet), k=random.randint(1, 5)))

        col1 = misc + ' ' + col1
        col2 = misc + ' ' + col2

    col1_lines.append(col1)
    col2_lines.append(col2)


print("total: %i" % len(col1_lines))


def convert_bichig(line):
    # replace 0x202f with '_'
    line = line.replace(chr(0x202f), '_')
    # replace whitespace with '#'
    line = line.replace(' ', '#')

    return ' '.join(line)


def convert_cyrillic(line):
    # replace whitespace with '#'
    return ' '.join(line.replace(' ', '#'))


os.makedirs('dataset', exist_ok=True)
with open('dataset/train.cyrillic', 'a') as f:
    lines = [convert_cyrillic(line) for line in col1_lines[:-2000]]
    f.write('\n'.join(lines) + '\n')
with open('dataset/train.bichig', 'a') as f:
    lines = [convert_bichig(line) for line in col2_lines[:-2000]]
    f.write('\n'.join(lines) + '\n')
with open('dataset/valid.cyrillic', 'a') as f:
    lines = [convert_cyrillic(line) for line in col1_lines[-2000:-1000]]
    f.write('\n'.join(lines) + '\n')
with open('dataset/valid.bichig', 'a') as f:
    lines = [convert_bichig(line) for line in col2_lines[-2000:-1000]]
    f.write('\n'.join(lines) + '\n')
with open('dataset/test.cyrillic', 'a') as f:
    lines = [convert_cyrillic(line) for line in col1_lines[-1000:]]
    f.write('\n'.join(lines) + '\n')
with open('dataset/test.bichig', 'a') as f:
    lines = [convert_bichig(line) for line in col2_lines[-1000:]]
    f.write('\n'.join(lines) + '\n')
