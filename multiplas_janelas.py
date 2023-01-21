import PySimpleGUI as sg

sg.theme('Reddit')

# Para cada janela, criei uma função


def janela_principal():
    layout = [
        [sg.Text('Cadastro - Competição corrida 100km')],
        [sg.Button('Registrar participante'), sg.Button('Sair')]
    ]
    return sg.Window('Janela 1', layout=layout, finalize=True)


def janela_cadastro_participante():
    layout = [
        [sg.Text('Nome')],
        [sg.Input(key='usuario')],
        [sg.Button('Registrar')]
    ]
    return sg.Window('Janela 2', layout=layout, finalize=True)


# inicializar todas janelas que devem inicializar com o programa
janela_principal_, janela_cadastro_participante_ = janela_principal(), None
# ler eventos e valores
while True:
    window, event, values = sg.read_all_windows()  # permite criar mais de uma janela
    if event == sg.WIN_CLOSED:
        break
    elif window == janela_principal_ and event == 'Registrar participante':
        janela_cadastro_participante_ = janela_cadastro_participante()
        janela_principal_.close()  # Aqui podemos utilizar o método hide() no lugar do close(). O close() fecha a janela atual, o hide() apenas a esconde, caso eu queria...
        # retornar para tela anterior
    elif window == janela_cadastro_participante_ and event == 'Registrar':
        usuario = values['usuario']
        sg.popup(f'Participante {usuario} cadastrado com sucesso!')
        
        
        
        