import os
import time
code = { '0': '-----',  '1': '.----',  '2': '..---','3': '...--','4': '....-','5': '.....','6': '-....',
        '7': '--...',  '8': '---..','9': '----.',
        'a': '.-','b': '-...','c': '-.-.','d': '-..','e': '.','f': '..-.','g': '--.','h': '....','i': '..',
        'j': '.---','k': '-.-','l': '.-..','m': '--','n': '-.','o': '---','p': '.--.','q': '--.-','r': '.-.',
     	's': '...','t': '-','u': '..-','v': '...-','w': '.--','x': '-..-','y': '-.--',   'z': '--..', ' ':'_'
        }
name = input("Enter your name: ")
print (name)
for letter in name:
    print (": " + letter + "\n")
    for i in code[letter]:
        if i == '.':
            os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( .3, 650))
        elif i == '_':
            os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( .3, 1350))
        else:
            os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( .8, 950))
        time.sleep(.2)
