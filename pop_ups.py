import PySimpleGUI as sg

sg.theme('Reddit')

layout = [
    [sg.Text('Digite seu código de entrada'), sg.Input(key='codigo'), sg.Button('Validar')],
    [sg.Button('Escolher período'), sg.Text(key='escolha')],
    [sg.Button('Cadastrar participante'), sg.Text(key='participante')],
    [sg.Button('Escolher arquivo'), sg.Text(key='arquivo')],
    [sg.Button('Escolher pasta'), sg.Text(key='pasta')],
]

window = sg.Window('Validação', layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Validar':
        if values['codigo'] == 'XH11':
            sg.popup('Código válido!')
        else:
            sg.popup('Código inválido')
    elif event == 'Escolher período':
        resposta = sg.popup('Quando devo rodar a automação?',
                            custom_text=('manhã', 'tarde'))
        window['escolha'].update(resposta)
    elif event == 'Cadastrar participante':
        participante = sg.popup_get_text('Digite seu nome')
        window['participante'].update(participante)
        print(f'Você cadastrou {participante}')
    elif event == 'Escolher arquivo':
        arquivo = sg.popup_get_file('Escolher arquivo')
        window['arquivo'].update(arquivo)
        print(f'Arquivo escolhido: {arquivo}')
    elif event == 'Escolher pasta':
        pasta = sg.popup_get_folder('Escolha uma pasta')
        window['pasta'].update(pasta)
        print(f'Pasta escolhida: {pasta}')
        
        
        # DOCUMENTAÇÃO DOS POPS: https://www.pysimplegui.org/en/latest/#high-level-api-calls-popups