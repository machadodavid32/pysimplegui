import PySimpleGUI as sg

sg.theme('Reddit')

#Layout do menu

layout_menu = [
    ['Arquivo', ['Abrir', 'Salvar']],
    ['Editar', ['Alterar Imagem',['Alterar Cor', 'Alterar Tamanho'], 'Alterar Claridade']],
    ['Ajudar', ['Versão']]
]

# Layout principal

layout_principal = [
    [sg.Menu(layout_menu)],
    [sg.Text('Bem-vindo á este aplicativo')],
    [sg.Output(size=(40,10) )]

]

window = sg.Window('Exemplo menu', layout=layout_principal)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Alterar Claridade':
        print('Alterando a claridade da imagem')

    