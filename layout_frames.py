import PySimpleGUI as sg

# tema
sg.theme('Reddit')
# Defina layout das colunas
coluna_esquerda = [
    [sg.Text('Insira seu usuário')],
    [sg.Input()],
    [sg.Text('Insira sua senha')],
    [sg.Input(password_char='*')]
]
coluna_meio = [
    [sg.Output(size=(40, 10))]
]

coluna_direita = [
    [sg.Text('Qual site automatizar?')],
    [sg.Checkbox('Opção 1'), sg.Checkbox('Opção 3'), sg.Checkbox('Opção 3')]
]

layout_principal = [
    [sg.Frame('Configurações Login',coluna_esquerda),sg.Column(coluna_meio),sg.Frame('Configurações Sites',coluna_direita)],
    [sg.Button('Enviar')]
  
]
# janela
window = sg.Window('Janela', layout_principal)
# Ler eventos
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    else:
        print(event)