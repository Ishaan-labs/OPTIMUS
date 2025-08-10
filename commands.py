import os
import webbrowser
import pyautogui

# SCREENSHOT
ssnum = 1
def ss():
    global ssnum
    while True:
        if os.path.exists(f"\\Users\\DELL\\OneDrive\\Pictures\\Screenshots\\screenshot_{ssnum}.png"):
            ssnum+=1
        else:
            pyautogui.screenshot(f"\\Users\\DELL\\OneDrive\\Pictures\\Screenshots\\screenshot_{ssnum}.png")
            break

# OPENING PROGRAMS

def spotify():
    os.system("spotify")

def audiorelay():
    os.system(r'"C:\Program Files (x86)\AudioRelay\AudioRelay.exe"')

def chrome():
    webbrowser.open_new("https://www.google.com/")

def youtube():
    webbrowser.open_new("https://www.youtube.com/")

def telegram():
    webbrowser.open_new("https://web.telegram.org/k/")

def reddit():
    webbrowser.open_new("https://www.reddit.com/")


