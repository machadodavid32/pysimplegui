import PySimpleGUI as sg

usuarios = [
    {
         'usuario': 'david',
         'senha': '123'
    },
    {
        'usuario': 'aline',
        'senha': '456'
    }
]

LICENCAS = ['AAA-BBB', 'CCC-DDD']

def janela_login():
    layout = [
        [sg.Text('Digite seu usuario')],
        [sg.Input(key='usuario')],
        [sg.Text('Digite sua senha')],
        [sg.Input(key='senha')],
        [sg.Button('Login'), sg.Button('Sair')],
        [sg.Text(key='usuario_valido')]
    ]
    return sg.Window('Janela Login', layout=layout, finalize=True)


def janela_validacao_licenca():
    layout = [
        [sg.Text('Favor digitar sua licença para continuar')],
        [sg.Input(key='numero_licenca')],
        [sg.Button('Validar Licença')],
        [sg.Text(key='status_licenca')]
        
    ]
    return sg.Window('Confirmação de acesso', layout=layout, finalize=True)


def janela_configuracoes():
    layout = [
        [sg.Text('Qual site gostaria de automatizar?')],
        [sg.Radio('Site 1', group_id='sites', key='site1'),
         sg.Radio('Site 2', group_id='sites', key='site2'),
         sg.Radio('Site 3', group_id='sites', key='site3')
        ],
        [sg.Text('Quantas postagens devem ser feitas nestes?')],
        [sg.Slider(range=(1,100), orientation='h')],
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
                window['usuario_valido'].update(text_color='Usuario Inválido') 
        elif event == 'Sair':
            break
                           