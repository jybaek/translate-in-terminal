[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

# Translate Bot
This translator uses the `google translate api`. 
Do not open your browser for translation anymore. We do not like touching the mouse or annoying you.

## Installation
```bash
pip install terminal-translator
or
pip install git+https://github.com/jybaek/translate-in-terminal.git
```

if you want to build it by yourself. It's required to install `wheel`.
```bash
git clone https://github.com/jybaek/translate-in-terminal.git
cd translate-in-terminal
# pip install wheel
python setup.py bdist_wheel
pip install dist/ranslatebot-1.0.0-py3-none-any.whl -I # slush or back-slush
```

## Usage
You can type the message you want to translate behind. Analyzes the input language and automatically sets the language to be translated.
More convenient is the fact that you can see the translated results directly on the screen and even save it to the _clipboard_!
Unfortunately, this is only compatible with English and Korean.

Now, I look forward to the new world opening in your troubles.

### Using the user input to translate
The text can be more than one. **It does not have to be wrapped by quotation marks.**
```bash
$ translate "Hello World"
안녕 세계
# or
$ translate Hello World
안녕 세계
```

### Using clipboard data to translate
The data in clipboard must be a text format.
```bash
$ translate -c
# or
$ translate --clipboard
```

### Clipboard
The result translated text will be copied to clipboard.

### No showing output message
```bash
$ translate "Hi"
안녕

$ translate -d "Hi" 
 
$
```

### Help Message
```bash
$ translate --help
usage: translate [-h] [--text {comment,clipboard}] [--dumb] [data [data ...]]

Terminal translator

positional arguments:
  data                  The text to query.

optional arguments:
  -h, --help            show this help message and exit
  --text {comment,clipboard}
  --dumb, -d            No showing output data

```
