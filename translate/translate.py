# -*- coding: utf-8 -*-
import argparse
import pyperclip
from googletrans import Translator

LANG = {'ko': 'en', 'en': 'ko'}

try:
    pyperclip.paste()
    CLIPBOARD_MESSAGE = 'Using clipboard data.'
except pyperclip.PyperclipException:
    CLIPBOARD_MESSAGE = """
    This error should only appear on Linux (not Windows or Mac). 
    You can fix this by installing one of the copy/paste mechanisms:
    
    sudo apt-get install xsel to install the xsel utility.
    sudo apt-get install xclip to install the xclip utility.
    pip install gtk to install the gtk Python module.
    pip install PyQt4 to install the PyQt4 Python module.
    """
    del pyperclip


def translate(text: list):
    text = ' '.join(text)
    text = text.replace('\n', ' ')

    # Translating each text message
    translator = Translator()
    lang = translator.detect(text).lang
    if lang not in ('ko', 'en'):
        raise ValueError('Unknown language')
    data = translator.translate(text, dest=LANG[lang]).text
    return data


def clipboard():
    if 'pyperclip' not in globals():
        raise argparse.ArgumentError(None, CLIPBOARD_MESSAGE)
    text = pyperclip.paste()
    return [text]


class TranslateAction(argparse._StoreAction):
    def __init__(self, option_strings, dest, nargs=None, const=None,
                 default=None, type=None, choices=None, required=False,
                 help=None, metavar=None ):

        super(TranslateAction, self).__init__(
            option_strings=option_strings,
            dest=dest,
            nargs=nargs,
            const=const,
            default=default,
            type=type,
            choices=choices,
            required=required,
            help=help,
            metavar=metavar)

    def __call__(self, parser:argparse.ArgumentParser, namespace, values, option_string=None):
        text = values
        if 'clipboard' in namespace and getattr(namespace, 'clipboard'):
            text = clipboard()
        values = translate(text)
        setattr(namespace, self.dest, values)


def main():
    # Argparse Setting
    parser = argparse.ArgumentParser(description='Terminal translator',
                                     argument_default=argparse.SUPPRESS)
    parser.register('action', 'translate', TranslateAction)
    parser.add_argument('-c', '--clipboard', action='store_true',
                         help=CLIPBOARD_MESSAGE)
    parser.add_argument('-d', '--dumb', action='store_true', default=False,
                         help='No showing output data.')
    parser.add_argument('data', nargs='*', action='translate', default=None,
                        help='The text to query.')
    args = parser.parse_args()

    # Getting the text messages at which user selected
    if not args.data:
        raise parser.error('No text to translate.')

    if 'pyperclip' in globals():
        pyperclip.copy(args.data)

    if not args.dumb:
        print(args.data)

if __name__ == '__main__':
    main()
