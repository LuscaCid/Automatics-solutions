import pyautogui
import time
from pytesseract import pytesseract

def funcao_btn_imprimir():
    time.sleep(0.3)
    while True:
        if pyautogui.locateCenterOnScreen("impressaobtn.png", confidence=0.9):
            x, y = pyautogui.locateCenterOnScreen("impressaobtn.png", confidence=0.9)
            break
    time.sleep(0.2)
    pyautogui.click(x, y)

def continuacao_consulta(crm,especialidade,nomeMed,procedimentos,gratuidade,procedimentosPaciente):
    time.sleep(0.4)
    pyautogui.click(x=366, y=154)
    pyautogui.write(crm)
    pyautogui.click(x=442, y=155)
    time.sleep(0.8)
    i,j = pyautogui.locateCenterOnScreen("confirmacaomedico.png",confidence=0.9)
    pyautogui.click(i, j)
    time.sleep(0.5)
    pyautogui.scroll(-500)
    consu_cod = "0301010072"
    x, y = pyautogui.locateCenterOnScreen("codprocedimento.png", confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(0.1)
    pyautogui.write(consu_cod)
    pyautogui.click(x=290, y=454)
    time.sleep(1)
    pyautogui.scroll(-1000)
    time.sleep(0.5)
    x, y = pyautogui.locateCenterOnScreen("medoftalmo.png", confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(0.1)
    while pyautogui.locateCenterOnScreen("carregando.png",confidence=0.9):
        time.sleep(0.2)
    time.sleep(0.2)
    pyautogui.scroll(-500)
    time.sleep(0.2)
    x, y = pyautogui.locateCenterOnScreen("especialidade.png", confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(0.1)
    pyautogui.write(especialidade)
    pyautogui.press("enter")
    time.sleep(0.7)
    pyautogui.scroll(-1000)
    time.sleep(0.2)
    x, y = pyautogui.locateCenterOnScreen("proximo.png", confidence=0.9)
    time.sleep(0.1)
    pyautogui.click(x, y)
    time.sleep(2)
    if pyautogui.locateCenterOnScreen("ddd.png",confidence=0.9):
        pyautogui.press("enter")
        time.sleep(0.2)
        pyautogui.scroll(2000)
        pyautogui.doubleClick(x=803, y=600)
        pyautogui.press("backspace")
        pyautogui.click(803,550)
        time.sleep(1)
        pyautogui.scroll(-2000)
        x, y = pyautogui.locateCenterOnScreen("proximo.png", confidence=0.9)
        pyautogui.click(x,y)
    pyautogui.scroll(-500)
    if pyautogui.locateCenterOnScreen("okcrmbtn.png", confidence=0.9) == False: pyautogui.click(x=127, y=217)
    else:
        x,y = pyautogui.locateCenterOnScreen("okcrmbtn.png", confidence=0.9)
        pyautogui.click(x, y)
    time.sleep(0.5)
    if  pyautogui.locateCenterOnScreen("finalizar.png", confidence=0.9):
        x,y = pyautogui.locateCenterOnScreen("finalizar.png", confidence=0.9)
        pyautogui.click(x, y)
    else: pyautogui.click(x=1198, y=589)
    time.sleep(1.6)

    time.sleep(3.2)
    pyautogui.hotkey("ctrl","p")
    funcao_btn_imprimir()
    time.sleep(0.5)
    pyautogui.doubleClick(x=70, y=299)  # alocacao do proc
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.1)
    x, y = pyautogui.locateCenterOnScreen("icone-vida.png", region=(300, 0, 800, 40), confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(0.2)
    pyautogui.click(x=164, y=470)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.click(x=255, y=473)
    time.sleep(7.0)
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
        verifier = 0
        if i == 0:
            i = i + 1  # pq o primeiro eh inutil
            continue
        time.sleep(3)
        x, y = pyautogui.locateCenterOnScreen("selecionarProcedimento.png", confidence=0.9)
        pyautogui.click(x, y)
        if procedimentos[i] == "ceratoscopia":
            pyautogui.write("topografia")
        else:
            pyautogui.write(procedimentos[i])
        pyautogui.press("enter")
        time.sleep(0.3)

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
            time.sleep(0.2)

        time.sleep(3.0)

        if pyautogui.locateCenterOnScreen("sempactomunicipio.png", confidence=0.9):
            time.sleep(0.2)
            pyautogui.press("enter")
            gratuidade.append(procedimentos[i])
            verifier = 1
        pyautogui.scroll(-1000)
        if verifier == 0: procedimentosPaciente.append(procedimentos[i])
        i = i + 1

    time.sleep(3)
    if len(procedimentosPaciente) > 1 and procedimentosPaciente != "vetor":
        pyautogui.scroll(-500)
        time.sleep(0.2)
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
    time.sleep(0.3)
    pyautogui.doubleClick(x=86, y=213)
    pyautogui.hotkey("ctrl", "c")
    pyautogui.hotkey("ctrl", "w")
    time.sleep(0.3)

    # com o codigo de identificador copiado:
    x, y = pyautogui.locateCenterOnScreen("atende-icon.png", region=(100, 730, 1200, 49), confidence=0.9)
    pyautogui.click(x, y)
    pyautogui.press("f10")
    time.sleep(0.3)
    pyautogui.press("left")
    time.sleep(0.3)
    pyautogui.press("enter")
    time.sleep(0.3)
    pyautogui.press("f5")
    time.sleep(0.5)
    pyautogui.press("enter")
    pyautogui.hotkey("ctrl", "enter")
    time.sleep(0.2)
    pyautogui.write("consulta medica")
    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(0.2)
    pyautogui.press("TAB", 3)
    time.sleep(0.4)
    if nomeMed.startswith("gerda lucia"):
        pyautogui.write("gerda")
    else:
        pyautogui.write(nomeMed)
    time.sleep(0.3)
    pyautogui.press("down")
    time.sleep(0.4)
    pyautogui.press("f5")
    time.sleep(0.2)
    pyautogui.press("enter")
    time.sleep(0.2)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.2)
    pyautogui.press("enter")

    k = 759
    j = 576
    i = 1
    if len(procedimentosPaciente) > 1:
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
            if i == len(procedimentosPaciente) - 1:
                pyautogui.hotkey("ctrl","w")
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

    time.sleep(1)
    pyautogui.press("enter", 3)
    if len(gratuidade) > 1 and gratuidade != "vetor":  # se tiver algo  na gratuidade, é necessario lançar
        pyautogui.press("f9", 3)
        pyautogui.press("f10")
        time.sleep(0.2)
        pyautogui.press("f10")
        pyautogui.click(x=114, y=166)
        pyautogui.write("gratuidade")
        pyautogui.press("down")
        pyautogui.press("f5")
        time.sleep(0.3)
        pyautogui.press("enter")
        i = 1  # a posicao 0 tem "vetor"
        while i < len(gratuidade):
            pyautogui.press("f3")
            time.sleep(0.3)
            pyautogui.hotkey("ctrl", "enter")
            time.sleep(0.2)
            pyautogui.write(gratuidade[i])
            time.sleep(0.2)
            pyautogui.press("enter")
            time.sleep(0.2)
            pyautogui.press("enter")
            pyautogui.press("TAB", 3)
            pyautogui.write(nomeMed)
            pyautogui.press("down")
            pyautogui.press("f5")
            time.sleep(0.2)
            pyautogui.press("enter", 3)
            time.sleep(0.1)
            pyautogui.press("enter")
            time.sleep(0.3)
            pyautogui.press("f3")
            i = i + 1
        time.sleep(0.2)
        pyautogui.press("left")
        pyautogui.press("enter")
        pyautogui.press("f8")
        time.sleep(1.5)
        pyautogui.press("enter", 3)
        while pyautogui.locateCenterOnScreen("deseja-lancar-outra", confidence=0.9) is not True:
            time.sleep(0.2)
            print("carregando")
        pyautogui.press("enter")
    time.sleep(0.2)
    pyautogui.hotkey("f2")
    pyautogui.hotkey("f4")  #####
    x, y = pyautogui.locateCenterOnScreen("chrome-icon.png", region=(100, 730, 1200, 49), confidence=0.9)
    pyautogui.click(x, y)
    time.sleep(0.2)
    x, y = pyautogui.locateCenterOnScreen("icone-vida.png", region=(240, 0, 1000, 40), confidence=0.9)
    pyautogui.click(x,y)
    pyautogui.press("f5")
    pyautogui.scroll(2000)
    time.sleep(0.2)
    pyautogui.hotkey("ctrl", "1")
    time.sleep(0.1)
    pyautogui.click(x=717, y=430)
    pyautogui.moveTo(x, y - 90)
    pyautogui.scroll(-500)

#este comando direciona pro google com o vida ja aberto e ja logado
x,y = pyautogui.locateCenterOnScreen("atende-icon.png",region=(100,730,1200,49),confidence=0.9)
pyautogui.click(x,y)
pyautogui.press("f4")
x,y = pyautogui.locateCenterOnScreen("chrome-icon.png",region=(100,730,1200,49),confidence=0.9)
pyautogui.click(x,y)
time.sleep(0.2)#precisa-se esperar as coisas acontecerem
#este comando seleciona a primeira guia onde deve estar localizado o vida - amb
pyautogui.hotkey("ctrl","1")
pyautogui.moveTo(x, y-90)
pyautogui.scroll(-500)
time.sleep(0.4)
pacientes = []
procedimentos =[]
procedimentos.append("vetor")
gratuidade = []
gratuidade.append("vetor")
procedimentosPaciente = []
procedimentosPaciente.append("vetor")
#criacao do menu onde o usuario vai inserir o registro
while True:
    opcao = int(input("1.Cobrar pacientes(consulta médica):\n0.Sair do programa:"))
    if opcao == 1:
        while True:
            reg = input("\ninforme os registros dos pacientes para cobra-los:\ndigite 1 para finalizar:")
            if reg == "1": break
            pacientes.append(reg)

    elif opcao == 0: break
    else: print("ocpao invalida")
    nomeMed = input("\nInforme o nome do medico (demanda aberta):")
    crm = input("\nInforme o CRM do medico responsável:")
    especialidade = input("Informe a especialidade por extenso:")
    while True:
        proc = input("Informe corretamente os nomes dos procedimentos que serão lançados (exceto consulta medica\ndigite 1 para finalizar)")
        if proc != "1": procedimentos.append(proc)
        else: break;
    isgrat = int(input("Informe se haverá o lançamento da gratuidade.\n1.sim\t2.não"))
    if isgrat == 1:
        while True:
            grat = input("Informe o(s) nome(s) do(s) procedimento(s):\nDigite 1 para finalizar:")
            if grat == "1": break
            gratuidade  .append(gratuidade)
#começo da cobrança
if len(pacientes) > 0:
    cont =0
    while cont < len(pacientes):#secao onde irei entrar no smart e pesquisa r
        time.sleep(0.5)
        x,y = pyautogui.locateCenterOnScreen("atende-icon.png",region=(100,730,1200,49),confidence=0.9)
        pyautogui.click(x,y)
        time.sleep(0.5)
        pyautogui.press("f2")
        time.sleep(0.2)
        pyautogui.press("f4")
        time.sleep(0.4)
        pyautogui.hotkey("shift","TAB")
        time.sleep(0.2)
        pyautogui.write(pacientes[cont])

        pyautogui.press("f4")
        time.sleep(0.2)
        pyautogui.press("left")
        time.sleep(0.2)
        pyautogui.press("enter")
        time.sleep(0.3)
        pyautogui.press("f10")
        time.sleep(0.2)
        pyautogui.press("left")
        time.sleep(0.1)
        pyautogui.press("enter")
        time.sleep(0.2)
        pyautogui.click(x=437, y=265)
        pyautogui.press("TAB")
        time.sleep(0.2)
        pyautogui.hotkey("ctrl","c")
        time.sleep(0.3)
        x, y = pyautogui.locateCenterOnScreen("chrome-icon.png", region=(100, 730, 1200, 49), confidence=0.9)
        pyautogui.click(x, y)
        time.sleep(0.5)
        pyautogui.click(x=302, y=557)
        time.sleep(0.5)
        pyautogui.click(x=252, y=401)
        pyautogui.hotkey("ctrl","v")
        time.sleep(0.5)
        pyautogui.click(x=144, y=537)
        time.sleep(2)
        pyautogui.scroll(-500)
        time.sleep(0.4)#momento onde há a procura pelo botao verdin
        sc = pyautogui.screenshot()
        altura, largura = sc.size
        isfind = False
        for i in range(0, altura, 5):
            for j in range(0, largura, 5):
                r, g, b = sc.getpixel((i, j))
                if r == 8 and g == 139 and b == 25:  # momento onde o botao eh encontrado
                    x, y = i, j
                    isfind = True
                    break
            if r == 8 and g == 139 and b == 25:
                break
        if isfind:
            pyautogui.click(i, j)
            time.sleep(3.2)
            pyautogui.scroll(-1000)
            time.sleep(0.2)
            x, y = pyautogui.locateCenterOnScreen("proximo.png", confidence=0.9)
            pyautogui.click(x, y)
            time.sleep(2)
            x, y = pyautogui.locateCenterOnScreen("agendado.png", confidence=0.9)
            pyautogui.click(x, y)
            time.sleep(1.1)
            continuacao_consulta(crm,especialidade,nomeMed,procedimentos,gratuidade,procedimentosPaciente)
            continue

        else:  # momento onde nao foi encontrado pelo cpf pois o botao nao apareceu
            print("nao foi encontrado")
            pyautogui.press("f5")
            time.sleep(0.9)
            pyautogui.scroll(1000)
            x,y = pyautogui.locateCenterOnScreen("atende-icon.png",region=(100,730,1200,49),confidence=0.9)
            pyautogui.click(x,y)
            time.sleep(0.2)
            pyautogui.click(x=109, y=268)
            time.sleep(0.1)
            pyautogui.hotkey("ctrl","c")
            x, y = pyautogui.locateCenterOnScreen("chrome-icon.png", region=(100, 730, 1200, 49), confidence=0.9)
            pyautogui.click(x, y)
            pyautogui.moveTo(x, y - 90)
            time.sleep(0.3)

            time.sleep(0.2)
            pyautogui.scroll(-500)
            time.sleep(0.3)
            if pyautogui.locateCenterOnScreen("botao-sus.png", confidence=0.9):
                x, y = pyautogui.locateCenterOnScreen("botao-sus.png", confidence=0.9)
                pyautogui.click(x,y)
            else: pyautogui.click(x=164, y=514)
            time.sleep(0.5)
            pyautogui.click(x=202, y=360)
            pyautogui.hotkey("ctrl", "v")
            pyautogui.click(x=144, y=537)
            time.sleep(2)
            pyautogui.scroll(-500)
            time.sleep(0.4)  # momento onde há a procura pelo botao verdin
            sc = pyautogui.screenshot()
            isfind = False
            for i in range(0, altura, 5):
                for j in range(0, largura, 5):
                    r, g, b = sc.getpixel((i, j))
                    if r == 8 and g == 139 and b == 25:  # momento onde o botao eh encontrado
                        x, y = i, j
                        isfind = True
                        break
                if r == 8 and g == 139 and b == 25:
                    break
            if isfind: #é pq foi encontrado pelo cns
                pyautogui.click(i, j)
                time.sleep(3.2)
                pyautogui.scroll(-1000)
                time.sleep(0.2)
                x, y = pyautogui.locateCenterOnScreen("proximo.png", confidence=0.8)
                pyautogui.click(x, y)
                time.sleep(1)
                x, y = pyautogui.locateCenterOnScreen("agendado.png", confidence=0.8)
                pyautogui.click(x, y)
                continuacao_consulta(crm,especialidade,nomeMed,procedimentos,gratuidade,procedimentosPaciente)
                continue

            else: #nao tem pacto, lanca tudo na gratuidade
                print("n tem pacto")
                gratuidade = procedimentos
                x, y = pyautogui.locateCenterOnScreen("atende-icon.png", region=(100, 730, 1200, 49), confidence=0.9)
                pyautogui.click(x, y)

                pyautogui.press("f10")
                time.sleep(0.2)
                pyautogui.press("left")
                time.sleep(0.1)
                pyautogui.press("enter")
                time.sleep(0.1)
                pyautogui.click(x=139, y=169)
                pyautogui.write("gratuidade")
                pyautogui.press("down")
                pyautogui.press("f5")
                time.sleep(0.2)
                i = 0
                contador = 0
                while i < len(gratuidade):
                    if i == 0:
                        pyautogui.press("enter")
                        time.sleep(0.1)
                        pyautogui.hotkey("ctrl", "enter")
                        time.sleep(0.1)
                        pyautogui.write("consulta medica")
                        time.sleep(0.1)
                        pyautogui.press("enter")
                        time.sleep(0.1)
                        pyautogui.press("enter")
                        pyautogui.press("TAB", 3)
                        pyautogui.write(crm)
                        pyautogui.press("TAB")
                        pyautogui.press("f5")
                        time.sleep(0.2)
                        pyautogui.press("left")
                        pyautogui.press("enter")
                        time.sleep(0.2)
                        pyautogui.press("enter", 2)
                        i = i + 1
                        continue

                    pyautogui.press("enter")

                    pyautogui.hotkey("ctrl", "enter")
                    time.sleep(0.1)
                    pyautogui.write(gratuidade[i])
                    pyautogui.press("enter")
                    pyautogui.press("enter")
                    pyautogui.press("TAB", 3)
                    pyautogui.write(crm)
                    pyautogui.press("TAB")
                    pyautogui.press("f5")
                    pyautogui.press("enter", 2)

                    time.sleep(0.5)

                    i = i + 1
                time.sleep(0.2)
                pyautogui.press("left")
                pyautogui.press("enter")
                pyautogui.press("f8")
                time.sleep(1.5)
                pyautogui.press("enter", 3)
                time.sleep(8)
                pyautogui.press("enter")
                pyautogui.press("f2")
                pyautogui.press("f4")
                # sc = pyautogui.screenshot(region=(50,120,700,270))
                # sc.save("teste-posicionamento.png")
    cont += 1