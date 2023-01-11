# spin são caixas de escolha que vai, por exemplo, de 1 até 9
# Comboboxes são as mesmas caixas, porém, ao clicar, o nome dos dados ja aparece

import PySimpleGUI as sg
# tema
sg.theme('Reddit')
# layout
layout = [
    [sg.Text('Escolha a velocidade de envio das mensagens'),sg.Spin(values=(1,2,3,4,5,6,7,8,9,10),initial_value=1)],
    [sg.Text('Escolha o perfil do usuário'),sg.Spin(values=('Iniciante','Intermediário','Avançado'),initial_value='Iniciante')],
    [sg.Text('Nível de assinatura'),sg.Combo(values=['Bronze','Prata','Ouro','Diamante'],default_value='Bronze')]
]
# janela
window = sg.Window('Automatizador',layout=layout)
# Loop de monitoramento de eventos
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break