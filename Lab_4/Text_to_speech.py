import pyttsx3 

tts = pyttsx3.init()
rate = tts.getProperty('rate')
tts.setProperty('rate', 200)
input=input("Enter your text: ")
tts.say(input)

tts.runAndWait() 