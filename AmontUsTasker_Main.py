# Controls Imports
import keyboard
import pyautogui

# General Imports
from PIL import Image
from time import sleep
import datetime
import os


# Own Imports
import AmontUsTasker_TaskChecker as AU_TskChk
import AmontUsTasker_TaskDoer as AU_Taskerss
import AmontUsTasker_UtilFunc as AU_Util




# Make sure the working directory is yourself.
import pathlib
PATH = pathlib.Path().resolve()
os.chdir(PATH)

os.system('mode con: cols=50 lines=30')
print('AutoTasker Started...')




OnMode = True
while True:
    sleep(0.01)
    if keyboard.is_pressed('shift+v') or keyboard.is_pressed('r+f'):
        print('shift+1  is pressed')
        if OnMode:
            OnMode=False
        else:
            OnMode=True
        print(f'    - Mode changed to {OnMode}')
        sleep(0.5)

    if OnMode:
        AU_TskChk.CheckForTask()

