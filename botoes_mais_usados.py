

import PySimpleGUI as sg


# Documentação dos botões

# Layout principal
sg.theme('Reddit')  # Tema
layout = [
    [sg.Button(button_text='Botão comum')],
    [sg.Cancel()],
    [sg.Ok()],
    [sg.Yes()],
    [sg.No()],
    [sg.Quit()],
    [sg.Exit()],
    [sg.Cancel('Cancelar')],
    [sg.CalendarButton('Escolha uma data', target='alvo1'),sg.Input(key='alvo1', size=(20, 1))],
    [sg.ColorChooserButton('Escolha uma cor', target='alvo2'),sg.Input(key='alvo2', size=(30, 1))],
    [sg.FileBrowse('Escolher arquivo', target='alvo3'),sg.Input(key='alvo3', size=(30, 1))],
    [sg.FilesBrowse('Escolher arquivos', target='alvo4',),sg.Input(key='alvo4', size=(30, 10))],
    [sg.FolderBrowse('Escolher pasta', target='alvo5',),sg.Input(key='alvo5', size=(30, 10))],
    [sg.Button('Enviar')]
]
# Criar janelas
janela = sg.Window('Janela', layout)
# Windows
while True:
    event, values = janela.Read()
    if event == sg.WIN_CLOSED:
        janela.close()
        break
    elif event == 'Enviar':
        print(values['alvo1'])
        print(values['alvo2'])
        print(values['alvo3'])
        print(values['alvo4'])
        print(values['alvo5'])
    else:
        print(event)