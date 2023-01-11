import PySimpleGUI as sg
# Tema
sg.theme('Reddit')
# Layout
layout = [
    [sg.Text('Digite um site')],
    [sg.Input(key='site')],
    [sg.Text('Digite seu nome')],
    [sg.Input(key='nome')],
    [sg.Text('Qual período deve rodar: Manhã ou Noite?')],
    [sg.Checkbox('Manha', key='manha'), sg.Checkbox('Noite', key='noite')],
    [sg.Text('Fazer pesquisas em quais sites')],
    [sg.Checkbox('Google', key='google'), sg.Checkbox(
        'Yahoo', key='yahoo'), sg.Checkbox('Bing', key='bing')],
    [sg.Text('Rodar programa de madrugada?')],
    [sg.Radio('Sim', group_id='horario', key='radio_sim'),
     sg.Radio('Não', group_id='horario', key='radio_nao')],
    [sg.Text('Velocidade')],
    [sg.Slider(range=(1, 100), default_value=1,
               orientation='h', key='velocidade')],
    [sg.Text('Dias')],
    [sg.Slider(range=(1, 31), default_value=14, orientation='h', key='dias')],
    
    [sg.Button(button_text='Enviar dados'), sg.Button(button_text='Salvar Configurações')]
    
]
# Janela
window = sg.Window('Buscador de Sites', layout=layout)
# Ler os valores da janela
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Enviar dados':
        print(event)
        print(values)
    elif event == 'Salvar Configurações':
        sg.popup('Configurações Salvas')
        
        