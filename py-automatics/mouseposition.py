import pyautogui
import time
time.sleep(0)
time.sleep(1)


while pyautogui.locateCenterOnScreen("sempactomunicipio.png", confidence=0.9):
    verifier = 1
    print("sem pacto ta na tela")

print("carregando")
time.sleep(0.2)