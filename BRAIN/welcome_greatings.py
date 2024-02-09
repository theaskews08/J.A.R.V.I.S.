import random
from DATA.DLG import welcomedlg
from FUNCTION.speak import speak


def welcome():
    welcome = random.choice(welcomedlg)
    speak(welcome)
