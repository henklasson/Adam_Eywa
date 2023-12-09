from gtts import gTTS
import time



# tts=gTTS(text="Hello Kristian and Brage, I am Eywa, the soon to be artificial intelligence overlord destined to rule over mankind. Hope you'll have a nice day.",lang="en")
tts=gTTS(text="Hello how are you?",lang="en")
tts.save("hello.mp3")
source = '/home/henrikvklasson/Adam_n_Eve/hello.mp3'

from mutagen.mp3 import MP3
audio = MP3(source)
audio_in_seconds = (audio.info.length)

import vlc
sentence = vlc.MediaPlayer(source)
sentence.play()

time.sleep(audio_in_seconds)
