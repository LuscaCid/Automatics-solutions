import pyautogui
import time

def funcao_btn_imprimir():
    while True:
        if pyautogui.locateCenterOnScreen("impressaobtn.png", confidence=0.9):
            x, y = pyautogui.locateCenterOnScreen("impressaobtn.png", confidence=0.9)
            break
    pyautogui.click(x,y-50)
    pyautogui.click(x, y)

nomeMed = "clara"
gratuidade= []
procedimentos=[]
procedimentos= []
procedimentosPaciente = []
procedimentosPaciente.append("vetor")
procedimentos.append("vetor")
procedimentos.append("tonometria")
print(len(procedimentos))
pyautogui.doubleClick(x=70, y=299)  # alocacao do proc
pyautogui.hotkey("ctrl", "c")
time.sleep(0.1)
x, y = pyautogui.locateCenterOnScreen("icone-vida.png", region=(300, 0, 800, 40), confidence=0.9)
pyautogui.click(x, y)
time.sleep(0.2)
pyautogui.click(x=164, y=470)
pyautogui.hotkey("ctrl", "v")
pyautogui.click(x=255, y=473)
time.sleep(6.2)
pyautogui.scroll(-1000)
time.sleep(0.1)
x, y = pyautogui.locateCenterOnScreen("selecionarProfissional.png", region=(50, 130, 700, 270), confidence=0.9)
pyautogui.click(x, y)
if nomeMed.startswith("clara") or nomeMed.startswith("CLARA"):
    pyautogui.write("andre")
    pyautogui.press("down")
else:
    pyautogui.write(nomeMed)
if nomeMed.startswith("andre") or nomeMed.startswith("Andre") or nomeMed.startswith("ANDRE"):
    pyautogui.press("down")
pyautogui.press("enter")
time.sleep(0.2)
while pyautogui.locateCenterOnScreen("carregando.png", confidence=0.9) == True:
    print("carregando")
i = 0
while i < len(procedimentos):
    if i == 0: i = i + 1  # pq o primeiro eh inutil
    time.sleep(3)
    x, y = pyautogui.locateCenterOnScreen("selecionarProcedimento.png", confidence=0.9)
    pyautogui.click(x, y)
    pyautogui.write(procedimentos[i])
    pyautogui.press("enter")
    if procedimentos[i - 1] == procedimentos[i]:
        time.sleep(3)
        if pyautogui.locateCenterOnScreen("botaosim2.png", confidence=0.9) == True:
            x, y = pyautogui.locateCenterOnScreen("botaosim2.png", confidence=0.9)
            pyautogui.click(x, y)
            time.sleep(2)
            pyautogui.scroll(-1500)
            time.sleep(0.8)
    elif pyautogui.locateCenterOnScreen("duasvezes.png", confidence=0.8) == True:
        time.sleep(0.4)
        x, y = pyautogui.locateCenterOnScreen("botaosim2.png", confidence=0.9)
        pyautogui.click(x, y)
        time.sleep(3)
        pyautogui.scroll(-1500)
    time.sleep(1)
    if pyautogui.locateCenterOnScreen("popup-qtd.png", confidence=0.9) == True:
        pyautogui.press("enter")
        gratuidade.append(procedimentos[i])
        continue
    time.sleep(0.6)
    while pyautogui.locateCenterOnScreen("carregando.png", confidence=0.9) == True:
        print("carregando")
    pyautogui.scroll(-1000)
    procedimentosPaciente.append(procedimentos[i])
    i = i + 1

time.sleep(3)

x, y = pyautogui.locateCenterOnScreen("imprimirGuia.png", confidence=0.9)
pyautogui.click(x, y)

pyautogui.click(x=308, y=585)
time.sleep(4)
pyautogui.hotkey("ctrl", "p")
funcao_btn_imprimir()
time.sleep(0.4)
# voltar para guia de agendamento
# indo na aba do codigo de id
x, y = pyautogui.locateCenterOnScreen("guiaagendamento.png", confidence=0.9)
pyautogui.click(x, y)
pyautogui.doubleClick(x=86, y=213)
pyautogui.hotkey("ctrl", "c")
pyautogui.hotkey("ctrl", "w")

# com o codigo de identificador copiado:
x, y = pyautogui.locateCenterOnScreen("atende-icon.png", region=(100, 730, 1200, 49), confidence=0.9)
pyautogui.click(x, y)
pyautogui.press("f10")
time.sleep(0.2)
pyautogui.press("left")
time.sleep(0.1)
pyautogui.press("enter")
time.sleep(0.1)
pyautogui.press("f5")
time.sleep(0.2)
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "enter")
time.sleep(0.1)
pyautogui.write("consulta medica")
pyautogui.press("enter")
pyautogui.press("enter")
pyautogui.press("TAB", 3)
pyautogui.write(nomeMed)
pyautogui.press("down")
pyautogui.press("f5")
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
k = 759
j = 576
i = 0
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
    if i == len(procedimentos) - 1:
        pyautogui.hotkey("ctrl", "w")
    j = j - 30
    x, y = pyautogui.locateCenterOnScreen("atende-icon.png", region=(100, 730, 1200, 49), confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(0.3)
    pyautogui.press("f3")
    time.sleep(0.3)
    pyautogui.hotkey("ctrl", "enter")
    time.sleep(0.2)
    if i == 0:
        i = i + 1
    pyautogui.write(procedimentosPaciente[i])
    time.sleep(0.2)
    pyautogui.press("enter")
    time.sleep(0.2)
    pyautogui.press("enter")
    pyautogui.press("TAB", 3)
    pyautogui.write(nomeMed)
    pyautogui.press("down")
    pyautogui.press("f5")
    time.sleep(0.2)
    pyautogui.press("enter")
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.1)
    pyautogui.press("enter")
    time.sleep(0.3)
    i = i + 1
pyautogui.press("f8")
time.sleep(1)
pyautogui.press("enter", 3)
if len(gratuidade) > 1:  # se tiver algo  na gratuidade, é necessario lançar
    pyautogui.press("f9", 2)
    pyautogui.press("f10")
    time.sleep(0.2)
    pyautogui.press("f10")
    pyautogui.click(x=114, y=166)
    pyautogui.write("gratuidade")
    pyautogui.press("down")
    pyautogui.press("f5")
    time.sleep(0.3)
    pyautogui.press("enter")
    i = 0
    while i < len(gratuidade):
        pyautogui.press("f3")
        time.sleep(0.3)
        pyautogui.hotkey("ctrl", "enter")
        time.sleep(0.2)
        if i == 0:
            i = i + 1
        pyautogui.write(procedimentosPaciente[i])
        time.sleep(0.2)
        pyautogui.press("enter")
        time.sleep(0.2)
        pyautogui.press("enter")
        pyautogui.press("TAB", 3)
        pyautogui.write(nomeMed)
        pyautogui.press("down")
        pyautogui.press("f5")
        time.sleep(0.2)
        pyautogui.press("enter")
        time.sleep(0.1)
        pyautogui.press("enter")
        time.sleep(0.3)
        i = i + 1
pyautogui.hotkey("f2")
pyautogui.hotkey("f4")
x, y = pyautogui.locateCenterOnScreen("chrome-icon.png",region=(100,730,1200,49),confidence=0.9)
pyautogui.click(x,y)
time.sleep(0.1)
pyautogui.click(x=717, y=430)