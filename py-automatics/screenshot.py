import pyautogui
import time
from pytesseract import pytesseract
time.sleep(1)
sc = pyautogui.screenshot(region=(240, 0, 1000, 40))
sc.save("posicao-do-icone.png")