from matplotlib.pyplot import text
import pyttsx3

text_speech = pyttsx3.init()

answer = input("Enter:")

text_speech.say(answer)

text_speech.runAndWait()