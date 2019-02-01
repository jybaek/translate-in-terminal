[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

# Translate Bot
This translator uses the `google translate api`. 
Do not open your browser for translation anymore. We do not like touching the mouse or annoying you.

## How do I use it?
Clone source code first. Of course, it is better to press star before that.
```bash
git clone https://github.com/jybaek/translate-in-terminal.git
```

Then run the `install.sh` script.
```bash
sh install.sh
```

Next, you need to have the `bin` folder under your _${HOME}_ directory, which should be included in your `PATH`. This is basically what most systems do, but if not, set it yourself.

Now, that's it. Use the `.translate` command on the terminal.
```bash
$ .translate
Usage: /Users/caley/bin/.translate "User message"
```

You see? You can type the message you want to translate behind. Analyzes the input language and automatically sets the language to be translated.
More convenient is the fact that you can see the translated results directly on the screen and even save it to the _clipboard_!
Unfortunately, this is only compatible with English and Korean.

Now, I look forward to the new world opening in your troubles.

```bash
$ .translate "안녕하세요"
Hi
$ .translate "hello"
여보세요
$ pbpaste
여보세요
```
