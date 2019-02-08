[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

# Translate Bot
This translator uses the `google translate api`. 
Do not open your browser for translation anymore. We do not like touching the mouse or annoying you.

## Installation
```bash
pip install translatebot
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
$ python translatebot.py "Hello World"
안녕 세계
# or
$ python translatebot.py Hello World
안녕 세계
```

### Using clipboard data to translate
The data in clipboard must be a text format.
```bash
$ python translatebot.py -c
# or
$ python translatebot.py --clipboard
```

### Clipboard
The result translated text will be copied to clipboard.

### No showing output message
```bash
$ python translatebot.py "Hi"
안녕

$ python translatebot.py -d "Hi" 
 
$
```

### Help Message
```bash
$ python translatebot.py --help
usage: translatebot.py [-h] [--text {comment,clipboard}] [--dumb]
                       [data [data ...]]

Audio editor

positional arguments:
  data                  The text to query.

optional arguments:
  -h, --help            show this help message and exit
  --text {comment,clipboard}
  --dumb, -d            No showing output data

```
