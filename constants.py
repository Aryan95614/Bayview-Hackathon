

import PySimpleGUI as sg


def a(dat):
    layout = [[sg.Text("Info for all COVID patients")],
              ([sg.Text(dat[i])] for i in range(len(dat))),
              [sg.Button("OK")]]

    window = sg.Window("Demo", layout, size = (500, 500))

    while True:
        event, values = window.read()

        if event == "OK" or event == sg.WIN_CLOSED:
            break

    window.close()

