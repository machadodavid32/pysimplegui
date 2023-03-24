import PySimpleGUI as sg

sg.theme('Reddit')


def janela_inicial():
    layout = [
        [sg.Text('Janela Inicial')],
        [sg.Input()],
        [sg.Button('Próximo >'), sg.Button('Sair')]
    ]
    return sg.Window('Janela Inicial', layout=layout, finalize=True)


def janela_sites():
    layout = [
        [sg.Text('Janela Sites')],
        [sg.Text('Quais sites devem ser automatizados?')],
        [sg.Checkbox('Site 1'), sg.Checkbox('Site 2')],
        [sg.Button('< Anterior'), sg.Button('Próximo >')]
    ]
    return sg.Window('Janela Sites', layout=layout, finalize=True)


def janela_configuracoes():
    layout = [
        [sg.Text('Janela Configurações')],
        [sg.Text('Receber notificação de conclusão da automação?')],
        [sg.Radio('Sim', group_id='notificao'),
         sg.Radio('Não', group_id='notificacao')],
        [sg.Button('< Anterior'), sg.Button('Finalizar Configurações')]
    ]
    return sg.Window('Janela configurações', layout=layout, finalize=True)


janela_inicial_, janela_sites_, janela_configuracoes_ = janela_inicial(), None, None  # serve para iniciar somente a primeira janela inicial

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED:
        break
    elif window == janela_inicial_:
        if event == 'Próximo >':
            janela_inicial_.hide()  # esconder a janela atual
            if janela_sites_:
                janela_sites_.un_hide()  # faz aparecer a janela_sites_
            else:
                janela_sites_ = janela_sites() 
        elif event == 'Sair':
            break

    elif window == janela_sites_:
        if event == '< Anterior':
            janela_sites_.hide()
            janela_inicial_.un_hide()
        elif event == 'Próximo >':
            janela_sites_.hide()
            if janela_configuracoes_:
                janela_configuracoes_.un_hide()
            else:
                janela_configuracoes_ = janela_configuracoes()
    elif window == janela_configuracoes_:
        if event == '< Anterior':
            janela_configuracoes_.hide()
            janela_sites_.un_hide()
        elif event == 'Finalizar Configurações':
            break