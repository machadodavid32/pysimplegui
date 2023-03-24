import sys
from cx_Freeze import setup, Executable

build_exe_options = {'packages': ['os'], 'includes': ['tkinter']}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name='Automatizador de sites',
    version='1.0',
    description='Uma aplicação que automatiza sites',
    options={'build.exe':build_exe_options},
    executables=[Executable('executavel.py', base=base)]
)    
