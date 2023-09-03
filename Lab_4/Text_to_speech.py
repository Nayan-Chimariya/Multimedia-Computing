import pyttsx3 

def text_to_speech(text,rate=0):  
    """Generates Speech for your text

    Args:
        text (str): Enter the text for speech generation
        rate (int, optional): Enter speech rate. Defaults to 0.
    """
    #* Initializing the engine for text to speech
    tts = pyttsx3.init()
    default_rate = tts.getProperty('rate')
    tts.setProperty('rate',default_rate+rate)
    tts.say(text)

    #TODO tts.save_to_file('Hello my name is nayan' , 'test.mp3')

    tts.runAndWait() 

#* Documentation in further examples 
#* [https://pyttsx3.readthedocs.io/en/latest/engine.html#examples]

text_to_speech("Hello World this is text to speech",200)