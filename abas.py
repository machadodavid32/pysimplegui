import PySimpleGUI as sg

# tema
sg.theme('Reddit')
# layout 
tab_cadastrado = [
    [sg.Text('Digite seu nome')],
    [sg.Input()],
    [sg.Text('Digite seu estado')],
    [sg.Input()],
    [sg.Button('Salvar Cadastro')]
]
tab_velocidade = [
    [sg.Text('Quantas buscas fazer por dia')],
    [sg.Slider(range=(1,10),default_value=1,orientation='v')],
    [sg.Button('Salvar Velocidade')]
]

layout_principal = [
    [sg.TabGroup([
        [sg.Tab('Cadastro',tab_cadastrado)],
        [sg.Tab('Velocidade',tab_velocidade)]
    ])]
]
# janela
window = sg.Window('Configurações',layout=layout_principal)
# Leitura de eventos e valores
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    else:
        print(event)