import pyttsx3

# create an engine instance that will use the specified driver
engine = pyttsx3.init()

# change the speech rate
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

# change the voice of the speaker
voices = engine.getProperty('voices')
engine.setProperty('voice', 'TTS_MS_EN-US_ZIRA_11.0')

# use the 'say' method to queue a command 
# to speak an utterance
engine.say("Just gonna stand there and watch me burn?")
engine.say("Well, that's all right because I like the way it hurts")
engine.say("Just gonna stand there and hear me cry?")
engine.say("Well, that's all right because I love the way you lie")
engine.say("I love the way you lie")

# invoke the runAndWait() method
engine.runAndWait()