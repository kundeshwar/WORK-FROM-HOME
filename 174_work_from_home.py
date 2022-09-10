import pyautogui as pag
import time
pag.FAILSAFE = False
while True:
    time.sleep(8)
    for i in range(100):
        pag.moveTo( 0, i*5 )
    for i in range(4):
        pag.press("shift")