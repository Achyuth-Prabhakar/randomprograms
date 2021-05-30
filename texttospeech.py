from gtts import gTTS
from playsound import playsound

audio = 'speech.mp3'
language = 'en'
ent = input("Enter text:")
print(ent)
sp = gTTS(text= ent, lang= language, slow= False)

sp.save(audio)
playsound(audio)