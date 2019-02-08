import argparse
import pyperclip
from googletrans import Translator

LANG = {'ko': 'en', 'en': 'ko'}


def main():
    # Argparse Setting
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS,
                                     description='Terminal translator')
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
    text = ' '.join(text)
    if not text:
        raise parser.error('No text to translate.')

    # Translating each text message
    translator = Translator()
    lang = translator.detect(text).lang
    if lang not in ('ko', 'en'):
        raise ValueError('Unknown language')
    data = translator.translate(text, dest=LANG[lang]).text
    pyperclip.copy(data)

    if not args.dumb:
        print(data)


if __name__ == '__main__':
    main()
