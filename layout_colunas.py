import PySimpleGUI as sg

# tema
sg.theme('Reddit')
# layout - (criar um layout diff para cada coluna)
coluna_esquerda = [
    [sg.Text('Insira seu usuário')],
    [sg.Input()],
    [sg.Text('Insira sua senha')],
    [sg.Input(password_char='*')],
]
coluna_meio = [
    [sg.Output(size=(40, 10))]
]

coluna_direita = [
    [sg.Text('Qual site automatizar?')],
    [sg.Checkbox('Opção 1'), sg.Checkbox('Opção 2'), sg.Checkbox('Opção 3')]
]

layout_principal = [
    [sg.Column(coluna_esquerda), sg.Column(coluna_direita)],
    [sg.Column(coluna_meio)],
    [sg.Button('Enviar')]
]

# janela
window = sg.Window('Cadastros', layout=layout_principal)
# Laço de leitura de eventos e valores
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    else:
        print(event)