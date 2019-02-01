#-*- coding: utf-8 -*-
import argparse
from googletrans import Translator

parser = argparse.ArgumentParser(description='Audio editor')
parser.add_argument('--comments', type=str, default='Hello', help='The host to query.')
args = parser.parse_args()

if __name__ == '__main__':

    comments = args.comments.replace("\n", " ")
    translator = Translator()
    lang = translator.detect(comments).lang

    if lang == 'ko':
        print(translator.translate(comments, dest='en').text)
    elif lang == 'en':
        print(translator.translate(comments, dest='ko').text)
    else:
        print(' Error: Unknwon language')
