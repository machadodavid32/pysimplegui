import PySimpleGUI as sg

sg.theme('Reddit')

# layout do menu

layout_menu1 = [
    ['File', ['New File', 'Save', 'Save-as']],
    ['Edit', ['Size', ['Change Resolution', 'Change Height', 'Change Width']]],
    ['About', ['About Author']]
]

# Layout principal

layout_principal1 = [
    [sg.Menu(layout_menu1)],
    [sg.Text('Bem-vindo a este aplicativo')],
    [sg.Output(size=(40,10))]
]

window = sg.Window('App Desafio aula 23', layout=layout_principal1)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'About Author':
        print('Feito por David')
        
        