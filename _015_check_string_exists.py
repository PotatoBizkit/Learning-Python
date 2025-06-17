# Program to check if a word exists in a text
import re

text = "" # Paste text here

word = '' # Paste word you want to check here

if re.search(rf'\b{re.escape(word.lower())}\b' in text.lower()):
    print(word, 'exists')
else:
    print('shit doesn\'t exist buckaroo')