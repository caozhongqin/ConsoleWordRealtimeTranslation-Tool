import pyperclip
import regex
import time
import os

last_word = ''
while True:
    word = pyperclip.paste().strip(' \t\n\r')
    if word != last_word:
        last_word = word
        if regex.fullmatch(r'[a-zA-Z ]+', word):
            print(word)
            os.system('tl ' + word)
    time.sleep(0.5)
