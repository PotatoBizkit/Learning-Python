# Program to check if a word exists in a text
import re

text = "i am a good boy" # Paste text here

word = 'Good' # Paste word you want to check here

pattern = rf'\b{re.escape(word.lower())}\b'

if re.search(pattern, text.lower()):
    print(word, 'exists')
else:
    print('shit doesn\'t exist buckaroo')