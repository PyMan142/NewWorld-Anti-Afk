from pynput.keyboard import *
from random import randrange
import time

keyboard = Controller()

#  ======== settings ========
resume_key = Key.alt_l 
pause_key = Key.ctrl_l 
exit_key = Key.ctrl_r
#  ==========================

pause = True
running = True

def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")


def display_controls():
    print("// AfkGamer is running")
    print("// - Settings: ")
    print("// - Controls:")
    print("\t left Alt = Resume")
    print("\t left control = Pause")
    print("\t right control = Exit")
    print("-----------------------------------------------------")
    print('Press Left alt to start ...')

#  ======= Key Presses ======
press1 = "1"
press2 = "2"
#  ==========================

def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            keyboard.press(press1)
            keyboard.release(press1)

            time.sleep(randrange(300)) #random range of time in seconds (300 = 5 minutes)

            keyboard.press(press2)
            keyboard.release(press2)
            time.sleep(randrange(300))
    lis.stop()

if __name__ == "__main__":
    main()