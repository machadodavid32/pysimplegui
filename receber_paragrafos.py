import PySimpleGUI as sg

# Tema
sg.theme('Reddit')
# Layout
layout = [
    [sg.Text('Resumo do livro')],
    [sg.Multiline(autoscroll=True, size=(40, 5), key='resumo')],
    [sg.Button('Salvar')]

]
# Janela
window = sg.Window('Opções de Valores', layout)
# Ler os valores da janela
while True:
    event, values = window.Read()
    if event == 'Salvar':
        with open('dados.txt', 'a', encoding='utf-8', newline='') as arquivo:
            arquivo.write(values['resumo'])
    elif event == sg.WIN_CLOSED:
        break
