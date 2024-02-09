import threading
from Automation._intregation_automation import Automation
from BRAIN.brain import *
from DATA.DLG import *
from BRAIN.welcome_greatings import *
from BRAIN.wish_greatings import *
from BRAIN.advice import *
from BRAIN.jokes import *
from Automation.battery_plug_check import *
from Automation.battery_alert import *
from FUNCTION.function_intregation import Function_cmd
from FUNCTION.listen import listen, hearing
from FUNCTION.speak import speak


def comain():
    while True:
        text = listen().lower()
        text = text.replace(" jar","jarvis")
        Automation(text)
        Function_cmd(text)
        Greating(text)

        if text in bye_key_word:
            x = random.choice(res_bye)
            speak(x)
            break
        elif "jarvis" in text:
            response = brain_cmd(text)
            speak(response)
        else:
            pass


def main():
    while True:
        wake_cmd = hearing().lower()
        if wake_cmd in wake_key_word:
            welcome()
            comain()
        else:
            pass




def jarvis():
    t1 = threading.Thread(target=main)
    t2 = threading.Thread(target=battery_alert)
    t3 = threading.Thread(target=check_plugin_status)
    t4 = threading.Thread(target=advice)
    t5 = threading.Thread(target=jokes)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()


jarvis()