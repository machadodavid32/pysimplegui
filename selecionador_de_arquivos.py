import PySimpleGUI as sg

sg.theme('Reddit')

layout = [
    [sg.Text('Selecionar um arquivo')],
    [sg.FileBrowse('Selecionar arquivo', target='caminho_arquivo', file_types=(
        ('Arquivos de texto', '*.txt'), ('Imagens PNG', '*.png'), ('Imagens JPG', '*.jpg'), ('Todos arquivos', '*')))],
    [sg.Input(key='caminho_arquivo')],
    [sg.Button('Ler arquivo')],
    [sg.FilesBrowse('Selecionar arquivos', target='caminho_arquivos', file_types=(
        ('Arquivos de texto', '*.txt'), ('Imagens PNG', '*.png'), ('Imagens JPG', '*.jpg'), ('Todos arquivos', '*')))],
    [sg.Input(key='caminho_arquivos')],
    [sg.Button('Ler arquivos')],
    [sg.Output(size=(45, 10))]
]
# janela
window = sg.Window('Janela', layout)
# leitura de eventos e valores
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Ler arquivo':
        with open(values['caminho_arquivo'], 'r') as arquivo:
            for linha in arquivo:
                print(linha)
    elif event == 'Ler arquivos':
        caminhos = values['caminho_arquivos'].split(';')
        for caminho in caminhos:
            with open(caminho,'r') as arquivo:
                for linha in arquivo:
                    print(linha)