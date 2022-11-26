import pyaudio
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os

kayit = sr.Recognizer()

def dinleme(a=False):
    with sr.Microphone() as kaynak:
        if a:
            print(a)
        mikrofon = kayit.listen(kaynak)
        ses = ""

        try:
            ses = kayit.recognize_google(mikrofon,language="tr-TR")
        except sr.UnknownValueError:
            print("Asistan: Anlayamadım.")
        except sr.RequestError:
            print("Asistan: Sistem şu an çalışmıyor...")

        return ses

def konusma(metin):
    tts = gTTS(text=metin,lang="tr", slow=False)
    mp3 = 'konusma.mp3'
    tts.save(mp3)
    playsound(mp3)

def yanit(ses):
    if "abla" in ses:
        konusma("Hoş Geldin")
        print("Sesli Asistan Aktif")
        if "merhaba" in ses:
            konusma("Sana da merhaba dostum")
        if "kapat" in ses:
            konusma("Çıkış yapılıyor")
            quit()

print("Başlatıldı...")

while True:
    ses = dinleme()
    if bool(ses) == True:
        print(ses)
        ses = ses.lower()
        yanit(ses)
