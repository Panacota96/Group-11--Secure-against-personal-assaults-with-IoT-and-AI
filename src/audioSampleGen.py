import pyttsx3

engine = pyttsx3.init()
engine.say("Are you okay, Honey?")
engine.save_to_file("Are you okay, Honey?", "output.mp3")
engine.runAndWait()
