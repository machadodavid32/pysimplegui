import PySimpleGUI as sg

# Tema
sg.theme('Reddit')
# Layout
layout = [
    [sg.Text('Digite seu nome')],
    [sg.Input(key='nome')],
    [sg.Text('Digite sua idade')],
    [sg.Input(key='idade')],
    [sg.OK(), sg.Cancel(), sg.Button('Enviar dados')]
]
# Janela
window = sg.Window('Minha janela', layout)
# Leitura dos valores da tela
while True:
    event, values = window.Read()
    print(event)
    if event == sg.WIN_CLOSED:
        break
    elif event == 'OK':
        print(values['nome'])
        print(values['idade'])
    elif event == 'Enviar dados':
        if values['nome'] == 'jhonatan':
            print('usuário encontrado')
        else:
            print('usuário não encontrado')