import speech_recognition as sr
from gtts import gTTS
import webbrowser as wb
import os
import wikipedia
import pygame

def play_audio(file_path):
    pygame.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue


def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "voice.mp3"
    try:
        os.remove(filename)
    except OSError:
        pass
    
    tts.save(filename)
    play_audio(filename)
    if os.path.exists(filename):
        os.remove(filename)


def get_audio_text():
    r = sr.Recognizer()
    print('Listening...')
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

        try:
            said = r.recognize_google(audio)
            print(said)
            return said.lower()
        
        except sr.UnknownValueError:
            speak("Sorry, I did not get that.")
            
        except sr.RequestError:
            speak("Sorry, the service is not available")


def program():
    audio_text = get_audio_text()
    if 'open youtube' in audio_text:
        try:
            speak('opening youtube')
            wb.open('https://www.youtube.com/')
            
        except:
            speak('Sorry, something was wrong!')
    
    elif 'open instagram' in audio_text:
        try:
            speak('opening the instagram')
            wb.open('https://www.instagram.com/')
        except:
            speak('Sorry, something was wrong!')
    
    elif 'open facebook' in audio_text:
        try:
            speak('Opening facebook')
            wb.open('https://www.facebook.com/')
        except:
            speak('Sorry, something was wrong!')
    
    elif 'search' in audio_text:
        try:
            summ = wikipedia.summary(
                audio_text.replace('search', ''),
                sentences=2
            )
            print(summ)
            speak(summ)
            
        except Exception as e:
            speak('Desired Result Not Found')
        

if __name__ == '__main__':
    program()