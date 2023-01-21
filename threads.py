
"""Threads servem para que o programa não trave enquanto alguma tarefa que leva mais tempo está sendo executada."""

import PySimpleGUI as sg
from utilidades_threads import baixar_arquivo
from threading import Thread


sg.theme('Reddit')

layout = [
    [sg.Text('Usuario'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(password_char='*', key='senha')],  # para a senha não ficar visivel
    [sg.Button('Logar')],
    [sg.Button('Baixar Arquivos', key='baixar_arquivo')],
    [sg.Output(size=(60,10))]
    ]

window = sg.Window('Cadastro de usuario', layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event =='baixar_arquivo':
        thread_arquivo =Thread(target=baixar_arquivo, args=(window, 'imagem'), daemon=True)  # daemon > informa que esta Trhead será uma thred secundária além de garantir que, se existir..
        # ...uma thread primaria e se ela for fechada, as outras também serão, garantindo melhor desempenho de memoria.
        thread_arquivo.start()
        window['baixar_arquivo'].update(disabled=True)
        # Se o programa necessitar que uma thread inicie após o fechamento de outra thread, estes passos:
    elif event == 'arquivo_baixado':
        thread_arquivo.join()   # este comando vai obrigar a criação de uma thread somente quando a anterior for finalizada   
        window['baixar_arquivo'].update(disabled=False)
        print(values['arquivo_baixado'])
        
        