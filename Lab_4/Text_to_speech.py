import pyttsx3 

#* Initializing the engine for text to speech
tts = pyttsx3.init()

tts.say("Hello my name is nayan")

#TODO tts.save_to_file('Hello my name is nayan' , 'test.mp3')

tts.runAndWait() 

#* Documentation in further examples 
#* [https://pyttsx3.readthedocs.io/en/latest/engine.html#examples]