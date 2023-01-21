from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def baixar_arquivo(window, tipo_arquivo):
    print('Baixando arquivos')
    sleep(10)
    window.write_event_value('arquivo_baixado', f'Arquivo {tipo_arquivo} baixado com sucesso')  # Permite criar um evento neste momento
    
def logar(window, values):
    def iniciar_driver():
        chrome_options = Options()
        arguments = ['--lang=pt-BR', '--window-size=800,1000', '--incognito']
        for argument in arguments:
            chrome_options.add_argument(argument)

        chrome_options.add_experimental_option('prefs', {
            'download.prompt_for_download': False,
            'profile.default_content_setting_values.notifications': 2,
            'profile.default_content_setting_values.automatic_downloads': 1,

        })
        driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()), options=chrome_options)

        return driver

    driver = iniciar_driver()

    driver.get('https://cursoautomacao.netlify.app/login.html')
        
    usuario = driver.find_element(
        By.XPATH, "//input[@id='email']")
    
    senha = driver.find_element(
        By.XPATH, "//input[@id='senha']")
    
    botao_enviar = driver.find_element(By.XPATH, "//button[text()='Enviar']")
    usuario.send_keys(values['usuario'])  # para pegar os dados do usuario informados no programa
    sleep(2)
    senha.send_keys(values['senha'])
    sleep(2)
    botao_enviar.click()
    sleep(2)
    driver.close()
    
    window.write_event_value('login_finalizado', 'Login realizado com sucesso!')
    
   