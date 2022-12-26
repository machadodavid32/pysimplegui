import PySimpleGUI as sg

# Tema
sg.theme('Reddit')
# Layout
layout = [
    [sg.Text('Digite seu nome')],
    [sg.Input(key='nome')],
    [sg.Text('Digite sua idade')],
    [sg.Input(key='idade')],
    [sg.OK(), sg.Cancel(), sg.Button('Enviar dados', key='enviar_dados')],
    [sg.Text(key='resultado', size=(20, 1))]

]
# Janela
window = sg.Window('Minha janela', layout)
# Leitura dos valores da tela
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'OK':
        if int(values['idade']) >= 18:
            window['resultado'].update('Você é maior de idade')
            window['resultado'].update(text_color='black')
            window['enviar_dados'].update(disabled=False)

        elif int(values['idade']) < 18:
            window['resultado'].update('Você é menor de idade')
            window['resultado'].update(text_color='red')
            window['enviar_dados'].update(disabled=True)