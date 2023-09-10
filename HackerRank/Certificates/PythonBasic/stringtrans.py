#!/bin/python3

import math
import os
import random
import re
import sys

import string


#
# Complete the 'transformSentence' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def transformSentence(sentence_input):
    # Write your code here
    alpha_list = list(string.ascii_lowercase)
    sentence_splitted = sentence_input.split(' ')
    sentence_out = ''
    for sentence in sentence_splitted:
        sentence_changed = sentence[0]
        for idl, letter in enumerate(sentence):
            if idl>0:
                current = alpha_list.index(letter.lower())
                preceding = alpha_list.index(sentence[idl-1].lower())                
                if preceding<current:
                    sentence_changed += sentence[idl].upper()
                elif preceding>current:
                    sentence_changed += sentence[idl].lower()
                else:
                    sentence_changed += sentence[idl]
        sentence_out += sentence_changed +' '
    return sentence_out[:-1]


if __name__ == '__main__':

    sentence = 'coOL dog'
    result = transformSentence(sentence)
    print(result)

