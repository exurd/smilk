# smilk
[![the logo](https://raw.githubusercontent.com/exurd/smilk/master/docs/sm.png)](https://github.com/exurd/smilk/ "smilk - very useless indeed!")
###### for python 3+ (maybe 2 as well i have not tested it yet)
[![GitHub version](https://badge.fury.io/gh/exurd%2Fsmilk.svg)](https://github.com/exurd/smilk/releases/ "still in beta!") ![smilk](https://img.shields.io/badge/s-milk-blue "smilk") ![build status - i mean, it works](https://img.shields.io/badge/build%20status-i%20mean%2C%20it%20works-yellow "passing with flying colors, such as yellow.")

Adds milk to the end of the word. Currently, the program cannot do more than one word in a parameter.

Release executable was made with PyInstaller.

This program has been licensed with "Do What The F-ck You Want To Public License". In short, DO WHAT THE F-CK YOU WANT TO DO WITH THIS!

## Usage

Typing 'smilk' uses the default options:

```
>smilk
smilk
```

Use the -h parameter to get to the help screen:

```
usage: smilk [-h] [--word WORD] [--secondary_word SECONDARY_WORD]
                [--milk MILK] [--version]

optional arguments:
  -h, --help            show this help message and exit
  --word WORD, -w WORD  The word itself. No spaces!
  --secondary_word SECONDARY_WORD, -sw SECONDARY_WORD
                        Secondary word. Added after milk. Not used by default.
  --milk MILK, -m MILK  Milk. Default is milk.
  --spaced, -s          Adds spaces between the words.
  --version             show program's version number and exit
```

A valid command for smilk is:

```
>smilk -w chocolate
chocolatemilk
```

You can space the words apart by using --spaced:

```
>smilk -w chocolate --spaced
chocolate milk
```

You can use different words that are not milk by using the related arguments :

```
>smilk -w git -m hub -sw er
githuber
```
