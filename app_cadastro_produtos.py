import PySimpleGUI as sg
import os

#tema
sg.theme('Reddit')

#layoyt
layout = [
[sg.Text('Digite o nome do produto')],
[sg.Input(key='nome')],
[sg.Text('Digite o código do produto')],
[sg.Input(key='codigo')],
[sg.Text('Digite a quantidade do produto')],
[sg.Input(key='quantidade')],
[sg.Text('Digite o valor do produto')],
[sg.Input(key='valor')],   
[sg.Button('Cadastrar')]   
]

# Janela
window = sg.Window('Produtos', layout)

# Leitura dos valores

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Cadastrar':
        produto_nome = values['nome']
        produto_codigo = values['codigo']
        produto_quantidade = values['quantidade']
        produto_valor = values['valor']
        with open('produtos.txt', 'a', encoding='utf-8', newline='') as arquivo:
            arquivo.write(f'{produto_nome}, {produto_codigo}, {produto_quantidade}, {produto_valor}, {os.linesep}')
        
        sg.popup(
            f'Você cadastrou {produto_quantidade} unidades de {produto_nome}, com o valor unitário {produto_valor}'
        )
        window['nome'].update('')
        window['codigo'].update('')
        window['quantidade'].update('')    
        window['valor'].update('')    
        
        



