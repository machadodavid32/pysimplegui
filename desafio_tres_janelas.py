import PySimpleGUI as sg

sg.theme('Reddit')

usuarios = [
    {
        'usuario': 'jhonatan',
        'senha': '123456'
    },
    {
        'usuario': 'amanda',
        'senha': 'abc123'
    }
]

LICENCAS = ['XHASDI12-XHASDI12-XHASDI12-XHASDI12',
            'ASDASD-12ASDASD-1ASDAS-D1ADASD', '12341-23412-123D4S-1234S']


def janela_login():
    layout = [
        [sg.Text('Digite seu usuário')],
        [sg.Input(key='usuario')],
        [sg.Text('Digite sua senha')],
        [sg.Input(key='senha', password_char='*')],
        [sg.Button('Login'), sg.Button('Sair')],
        [sg.Text(key='usuario_valido')]
    ]

    return sg.Window('Janela Login', layout=layout, finalize=True)


def janela_validacao_licenca():
    layout = [
        [sg.Text('Favor digitar sua licença para continuar')],
        [sg.Input(key='numero_licenca')],
        [sg.Button('Validar licença')],
        [sg.Text(key='status_licenca')]

    ]
    return sg.Window('Confirmação de acesso', layout=layout, finalize=True)


def janela_configuracoes():
    layout = [
        [sg.Text('Qual site gostaria de automatizar?')],
        [sg.Radio('Site 1', group_id='sites', key='site1'), sg.Radio(
            'Site 2', group_id='sites', key='site2'), sg.Radio('Site 3', group_id='sites', key='site3')],
        [sg.Text('Quantas postagens devem ser feitas nestes sites?')],
        [sg.Slider(range=(1, 100), orientation='h')],
        [sg.Output(size=(45, 5))],
        [sg.Button('Iniciar')]
    ]

    return sg.Window('Janela Configurações', layout=layout, finalize=True)


janela_login_, janela_validacao_licenca_, janela_configuracoes_ = janela_login(), None, None

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED:
        break
    elif window == janela_login_:
        if event == 'Login':
            usuario_valido = False
            for usuario in usuarios:
                if usuario['usuario'] == values['usuario']:
                    if usuario['senha'] == values['senha']:
                        janela_login_.close()
                        janela_validacao_licenca_ = janela_validacao_licenca()
                        usuario_valido = True
            if usuario_valido == False:
                window['usuario_valido'].update(text_color='red')
                window['usuario_valido'].update('Usuário inválido')
        elif event == 'Sair':
            break
    elif window == janela_validacao_licenca_:
        if event == 'Validar licença':
            if values['numero_licenca'] in LICENCAS:
                janela_validacao_licenca_.close()
                janela_configuracoes_ = janela_configuracoes()
            else:
                janela_validacao_licenca_[
                    'status_licenca'].update(text_color='red')
                janela_validacao_licenca_[
                    'status_licenca'].update('Licença inválida')
    elif window == janela_configuracoes_:
        if event == 'Iniciar':
            print(f'Iniciando automação, usando os valores {values}')