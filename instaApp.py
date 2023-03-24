import PySimpleGUI as sg
from utilidades import instaauto
import webbrowser
import pyautogui
from time import sleep


sg.theme('LightBrown')

layout = [
    [sg.Text("Digite seu usuario: ")],
    [sg.Input(key='usuario')],
    [sg.Text('Digite sua senha: ')],
    [sg.Input(key='senha')],
    [sg.Button('Start')]    
]

window = sg.Window('InstaAuto', layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Start':
        instaauto()
        
        

