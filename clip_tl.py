import pyperclip
import regex
import time
import os

last_word = ''
while True:
    word = pyperclip.paste()
    if word != last_word:
        last_word = word
        if regex.fullmatch(r'\w+', word):
            print(word)
            os.system('tl ' + word)
    time.sleep(0.5)
