import PySimpleGUI as sg
import pyperclip

layout = [  [sg.Text('Insert path:')],
            [sg.Input(key='-IN-', right_click_menu=[[''], ['Paste']])],
            [sg.Button('Paste'),sg.Button('Slash (/)'),sg.Button('Slash (/) and copy')],
            [sg.Text(''), sg.Text(size=(15,1), key='-OUTPUT-')],
            [sg.Button('Copy'),sg.Button('Exit')]
            ]

window = sg.Window("Backslash replacer", layout, keep_on_top=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Paste':
        window['-IN-'].update(sg.clipboard_get())

    if event == 'Slash (/) and copy':
        text0 = values['-IN-'].replace("\\", "/")
        if not ("'" in text0 or '"' in text0):
            text0 = "'"+text0+"'"
        pyperclip.copy(text0)
        window['-OUTPUT-'].update(text0)
        
    if event == 'Slash (/)':
        text0 = values['-IN-'].replace("\\", "/")
        if not ("'" in text0 or '"' in text0):
            text0 = "'"+text0+"'"
        window['-OUTPUT-'].update(text0)

    if event == 'Copy':
        pyperclip.copy(text0)

window.close()
