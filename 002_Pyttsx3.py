import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #fem voice
engine.setProperty('rate', 95) #speech speed
engine.say("I love chainsaw man.")
engine.runAndWait()