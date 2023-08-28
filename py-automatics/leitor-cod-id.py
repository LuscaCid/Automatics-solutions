import time

import pyautogui
from pytesseract import pytesseract

tesseract_path = "C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe"  # Substitua pelo caminho correto no seu sistema

# Configure o caminho do Tesseract para pytesseract
pytesseract.tesseract_cmd = tesseract_path

cod_id = pytesseract.image_to_string("tester2.jpg")
codigo_id = []
for i in range(len(cod_id)):
    if i > 24 and len(codigo_id) < 15:
        if cod_id[i] == "0" or cod_id[i] == "1" or cod_id[i] == "2" or cod_id[i] == "3" or cod_id[i] == "4" or cod_id[i] == "5" or cod_id[i] == "6" or cod_id[i] == "7" or cod_id[i] == "8" or cod_id[i] == "9" or cod_id[i] == "1":
            codigo_id.append(cod_id[i])

j = 0
identificador = []

while j < len(codigo_id):
    if j > 0:
        identificador.append(codigo_id[j])
    j = j + 1
print(identificador)
if identificador[5] == "5":
    identificador[5] = "6"
x,y = pyautogui.locateCenterOnScreen("chrome-icon.png", region=(100, 730, 1200, 49), confidence=0.9)
pyautogui.click(x,y)
time.sleep(0.2)
x,y = pyautogui.locateCenterOnScreen("insercao-cod.png",confidence=0.9)
pyautogui.doubleClick(x,y)
time.sleep(0.2)
pyautogui.write(identificador)
x,y = pyautogui.locateCenterOnScreen("loopa-id.png",confidence=0.9)
pyautogui.click(x,y)
time.sleep(0.3)
while True:
    if pyautogui.locateCenterOnScreen("carregando.png",confidence=0.9) == True:
        print("carregando")
    else: break
pyautogui.scroll(-1000)
time.sleep(0.4)
x,y = pyautogui.locateCenterOnScreen("confirmar-execucao.png",confidence=0.9)
pyautogui.click(x,y)
time.sleep(0.8)
pyautogui.press("enter")
