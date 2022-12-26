import PySimpleGUI as sg

# Tema
sg.theme('Reddit')
# Layout
layout = [
    [sg.Text('Nome', size=(5, 1)), sg.Input(key='nome', size=(25, 1))],  # Aqui vamos mexer no tamanho dos elementos
    [sg.Text('Idade', size=(5, 1)), sg.Input(key='idade', size=(25, 1))], # Aqui vamos mexer no tamanho dos elementos
    [sg.Text('CPF', size=(5, 1)), sg.Input(key='cpf', size=(25, 1))], # Aqui vamos mexer no tamanho dos elementos
    [sg.Button(button_text='Cadastrar')]
]
# Janela

window = sg.Window('Tela de Cadastro', layout=layout)
# Leitura de eventos e valores
while True:
    event, values = window.read()
    # ler e reagir aos eventos
    if event == sg.WIN_CLOSED:
        break
    else:
        print(event)