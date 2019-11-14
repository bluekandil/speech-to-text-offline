import speech_recognition as sr
# obtain path to "english.wav" in the same folder as this script
from os import path
import sys
import os

audioClip="Evacuate.wav"
outputFile=os.path.splitext(audioClip)[0]

# output to textfile
def saveToFile(text):
    sys.stdout=open("transcribes/"+outputFile,"w")
    print (text)
    sys.stdout.close()
 
# def openFile():
#     os.startfile('transcribe.txt')
#     os.system("notepad.exe file.txt")

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "audioFiles/"+audioClip)
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

# recognize speech using Sphinx
try:
    # print("Sphinx thinks you said ..... " + r.recognize_sphinx(audio))
    saveToFile(r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))




# import speech_recognition as sr    
# #obtain path to "english.wav" in the same folder as this script
# from os import path
# AUDIO_FILE = path.join(path.dirname(path.realpath(file)), "english.wav")
# AUDIO_FILE = path.join(path.dirname(path.realpath(file)), "french.aiff")
# AUDIO_FILE = path.join(path.dirname(path.realpath(file)), "chinese.flac")
# #use the audio file as the audio source
# r = sr.Recognizer()
# with sr.AudioFile(AUDIO_FILE) as source:
#     audio = r.record(source) # read the entire audio file
#     #recognize speech using Sphinx
#     try:        
#         print("Sphinx thinks you said " + r.recognize_sphinx(audio))
#     except sr.UnknownValueError:
#         print("Sphinx could not understand audio")
#     except sr.RequestError as e:
#         print("Sphinx error; {0}".format(e))