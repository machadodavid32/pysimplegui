import PySimpleGUI as sg

# Tema
sg.theme('DarkPurple5')  # pegue o tema em : https://www.pysimplegui.org/en/latest/#themes-automatic-coloring-of-your-windows 
# layout

layout = [
    [sg.Text('Digite seu nome')],  # Aqui representa uma linha
    [sg.Input(key='nome')],  # Aqui representa outra linha
    [sg.Text('Digite sua idade')],
    [sg.Input(key='idade')],
    [sg.Button(button_text='Cadastrar')]   # E aqui outra linha
]

# janela
window = sg.Window('Tela de Cadastro', layout=layout)

# Leitura de eventos e valores
while True:
    event, values = window.read()
    # ler e reagir aos eventos
    if event == sg.WIN_CLOSED: # pessoa tentou fechar a janela
        break
    elif event == 'Cadastrar':
        nome = values['nome']
        idade = values['idade']
        print(f"Você cadastrou {nome}, {idade} anos")
        print(values)
        




