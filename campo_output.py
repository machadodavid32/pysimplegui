# output é quando, após um cadastro qualquer, aparece na tela os dados do cadastrado

# para este programa, vamos criar outro arquivo chamado utilidades.py com uma função para não travar a tela quando for efetuar o cadastro.

from concurrent.futures import thread
import PySimpleGUI as sg
from utilidades import baixar_arquivos
from threading import Thread

# tema
sg.theme('Reddit')
# layout
layout = [
    [sg.Text('Digite seu nome'), sg.Input(key='nome')],
    [sg.Button('Cadastrar')],
    [sg.Button('Baixar arquivos')],
    [sg.Output(size=(60, 5))]
]
# janela
window = sg.Window('Cadastro de usuário', layout=layout)
# Laço de leitura de eventos e valores
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Cadastrar':
        print(values['nome'])
    elif event == 'Baixar arquivos':
        thread_arquivos = Thread(target=baixar_arquivos, daemon=True)
        thread_arquivos.start()  # esse comando é usado para processos que demaram mais que, por exemplo, 10 segundos e serve para  que o programa não trave.

        