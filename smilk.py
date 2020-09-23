#            DO WHAT THE F*CK YOU WANT TO PUBLIC LICENSE
#                    Version 2, December 2004
#
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#            DO WHAT THE F*CK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE F*CK YOU WANT TO. Thank you for reading the license.

import argparse

parser = argparse.ArgumentParser(description='Adds milk to the end of the word. It will ignore any errors in the arguments. Currently, the program cannot do more than one word in a parameter. It can be changed with parameters if necessary.', epilog='This program has the WTFPL license. DO WHAT THE F*CK YOU WANT TO.')
parser.add_argument('--word', '-w', type=str,  help='The word itself. No spaces!', default='s')
parser.add_argument('--secondary_word', '-sw', type=str,  help='Secondary word. Added after milk. Not used by default.', default='')
parser.add_argument('--milk', '-m', type=str,  help='Milk. Default is milk.', default='milk')
parser.add_argument('--spaced', '-s',  help='Adds spaces between the words.', action='store_true')
parser.add_argument('--version', action='version', version='%(prog)s 0.1')
args, unknown = parser.parse_known_args()

if args.word == 'got' and args.spaced == True: # easter egg code
    print("got milk? i'm thirsty")
elif args.word == 'milk' and args.secondary_word == 'milk': # easter egg code
    if args.spaced == True:
        print("When you typed in the command, the word 'milk milk milk' came on the screen.")
    else:
        print("When you typed in the command, the word 'milkmilkmilk' came on the screen.")
    print("However, without realizing it, you accidentially created a black hole, which sucked you and everything into it.")
    print("GAME OVER")
    print("YOUR SCORE: 42")
    print("Want to play again?")
elif args.word == 'milk' and args.milk == 'milk' or args.secondary_word == 'milk' and args.milk == 'milk': # easter egg code
    if args.spaced == True:
        print(args.word, args.milk, args.secondary_word + "? isn't that a bit nonsensical?")
    else:
        print(args.word + args.milk + args.secondary_word + "? isn't that a bit nonsensical?")
else:
    if args.spaced == True:
        print(args.word, args.milk, args.secondary_word)
    else:
        print(args.word + args.milk + args.secondary_word)
    # this is it. there's nothing else.
