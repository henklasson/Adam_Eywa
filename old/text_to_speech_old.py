from gtts import gTTS
import os


tts=gTTS(text="Hello Kristian and Brage, I am Eywa, the soon to be artificial intelligence overlord destined to rule over mankind. Hope you'll have a nice day.",lang="en")
tts.save("hello.mp3")
source = '/home/henrikvklasson/Adam_n_Eve/hello.mp3'

#filename = '/home/henrikvklasson/Adam_n_Eve/hello.wav'
#music = pyglet.media.load(filename, streaming=False)
#music.play()

#os.system("/home/henrikvklasson/hello.mp3")
#subprocess.call(['xdg-open', '/home/henrikvklasson/Adam_n_Eve/hello.mp3'])

# Import the required module for text 
# to speech conversion
from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os
  
# The text that you want to convert to audio
mytext = 'Welcome to geeksforgeeks!'
  
# Language in which you want to convert
language = 'en'
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
  
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcome.mp3")
  
# Playing the converted file
os.system("start welcome.mp3")