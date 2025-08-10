import speech_recognition as sr
import pyttsx3

def inp():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 0.5)
        print("listening.....")

        try:
            global a
            a = r.listen(source,timeout = 5, phrase_time_limit= 2)
            print("ohh, ishan")
            print(a)

        except sr.WaitTimeoutError:
            print("give me command sir")

        except Exception as e :
            print("Something went wrong", e)

def out(b):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(b)
    engine.runAndWait()



