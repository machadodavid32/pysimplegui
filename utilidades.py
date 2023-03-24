from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


def baixar_arquivos():
    print('Baixando Arquvos')
    sleep(5)
    print('Arquivos baixados')
    
    
def extrair_precos(window):
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    driver.get('https://cursoautomacao.netlify.app/produtos1.html')

    precos = driver.find_elements(By.XPATH, "//p[@class='price-container']")

    lista_precos = []

    for preco in precos:
        lista_precos.append(preco.text)
    sleep(5)
    driver.close()

    window.write_event_value('automacao_finalizada', lista_precos)
    
    
    

# 1 - Navegar até o site https://www.instagram.com
def instaauto():

    import webbrowser
    import pyautogui
    from time import sleep

    while True:
        
        usuario = input("Informe o usuario: ")
        senha = input('Informe a sua senha: ')
        sleep(3)
        
        webbrowser.open_new_tab('https://www.instagram.com')
        sleep(1)
        
        # Trocar de conta
        pyautogui.click(1224,648, duration=2)
        
        # login
        pyautogui.click(1047,379,duration=2)
        pyautogui.typewrite(usuario)
        sleep(2)

        
        # Senha
        pyautogui.click(1135,419, duration=2)
        pyautogui.typewrite(senha)
        sleep(2)
    
        
        # Entrar
        pyautogui.click(1129,464, duration=1)
        sleep(2)
        
        # Não salvar
        pyautogui.click(1044,613, duration=1)
    
        # 2 - clicar em pesquisar
        pyautogui.click(54,282,duration=1.5)
        sleep(1)
        # Escrevendo o que pesquisar
        pyautogui.typewrite('ibm')
        
        # Clicando no resultado da pesquisa
        pyautogui.click(243,311, duration=1)
        sleep(1)
        
        
        # Mover até a publicação
        pyautogui.moveTo(682,761,duration=2)
        sleep(5)
        # Clicar na publicação
        pyautogui.click(683,768,duration=1)
        sleep(3)
        # Clicar em curtir
        #pyautogui.click(1115,869,duration=1)
        #sleep(2)
        
    
        # 10 - Verificar se já curti ou não aquela postagem
        coracao = pyautogui.locateCenterOnScreen('coracao.png')
        sleep(1)
        # 11 - Se já tiver curtido, fazer nada, e pausar o bot por 24 horas
        if coracao is not None:
            sleep(86400)
        # 12 - Se não tiver curtido, curtir a foto
        elif coracao == None:
            pyautogui.click(1140,866,duration=1)
            sleep(5)
            # 13 - Se não tiver curtido, comentar na foto
            pyautogui.click(1175,984,duration=1)
            sleep(3)
            pyautogui.typewrite('Legal!')
            sleep(5)
            pyautogui.click(1535,977,duration=1)
        
            sleep(3)    
            pyautogui.doubleClick(33,984, duration=2)
            sleep(3)
            pyautogui.click(46,922, duration=2)
            sleep(1)
            break