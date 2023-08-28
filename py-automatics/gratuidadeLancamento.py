import time
import pyautogui
crm = "13758"

procedimentos = []
procedimentos = "vetor", "tonometria"
gratuidade = []
gratuidade = "vetor", "biomicroscopia","biomicroscopia"
procedimentosPaciente = procedimentos
time.sleep(1.5)

x, y = pyautogui.locateCenterOnScreen("atende-icon.png", region=(100, 730, 1200, 49), confidence=0.9)
pyautogui.click(x, y)
#pyautogui.press("f10")
#time.sleep(0.3)
#pyautogui.press("left")
#time.sleep(0.3)
#pyautogui.press("enter")
#time.sleep(0.3)
#pyautogui.press("f5")
#time.sleep(0.5)
#pyautogui.press("enter")
pyautogui.hotkey("ctrl", "enter")
time.sleep(0.2)
pyautogui.write("consulta medica")
pyautogui.press("enter")
pyautogui.press("enter")
time.sleep(0.2)
pyautogui.press("TAB", 3)
time.sleep(0.2)
pyautogui.write(crm)
pyautogui.press("TAB")
pyautogui.press("f5")
time.sleep(0.4)
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
k = 759
j = 576
i = 1
while i < len(procedimentosPaciente):
    x, y = pyautogui.locateCenterOnScreen("chrome-icon.png", region=(100, 730, 1200, 49), confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(0.1)
    x, y = pyautogui.locateCenterOnScreen("demandaaberta.png", confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(0.4)
    pyautogui.doubleClick(k, j)
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.1)
    j = j - 30
    x, y = pyautogui.locateCenterOnScreen("atende-icon.png", region=(100, 730, 1200, 49), confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(0.3)
    pyautogui.press("f3")
    time.sleep(0.3)
    pyautogui.hotkey("ctrl", "enter")
    time.sleep(0.2)
    pyautogui.write(procedimentosPaciente[i])
    time.sleep(0.2)
    pyautogui.press("enter")
    time.sleep(0.2)
    pyautogui.press("enter")
    pyautogui.press("TAB", 3)
    pyautogui.write(crm)
    pyautogui.press("TAB")
    pyautogui.press("f5")
    time.sleep(0.2)
    pyautogui.press("enter")
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.1)
    pyautogui.press("enter")
    time.sleep(0.3)
    i = i + 1
