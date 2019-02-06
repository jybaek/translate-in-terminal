import argparse
import pyperclip
from googletrans import Translator

LANG = {'ko': 'en', 'en': 'ko'}


def main():
    # Argparse Setting
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS,
                                     description='Audio editor')
    parser.add_argument('--clipboard', '-c', action='store_true',
                        default=False, help='Using clipboard data.')
    parser.add_argument('data', default=None, nargs='*',
                        help='The text to query.')
    parser.add_argument('--dumb', '-d', action='store_true',
                        default=False, help='No showing output data.')
    args = parser.parse_args()

    # Getting the text messages at which user selected
    text = args.data
    if args.clipboard:
        text = [pyperclip.paste()]

    if not text:
        raise parser.error('No text to translate.')

    # Translating each text message
    data = list()
    translator = Translator()
    for t in text:
        lang = translator.detect(t).lang
        if lang not in ('ko', 'en'):
            raise ValueError('Unknown language')
        data.append(translator.translate(t, dest=LANG[lang]).text)
    data = ' '.join(data)
    pyperclip.copy(data)

    if not args.dumb:
        print(data)

if __name__ == '__main__':
    main()