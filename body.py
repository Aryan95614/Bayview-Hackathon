import PySimpleGUI as sg
import sys
from Hackathon.Network import Network


class Window():

    def c(self, elems):
        return (sg.Stretch(), *elems, sg.Stretch())

    def __init__(self):
        self.total = 0
        self.net = Network()

        self.changing = lambda x, y: y if self.events[x] else 0
        self.events = None

        self.layout = [
            [self.c([sg.Text('COVID AFFIRMERATOR 2000')])],
            [self.c([sg.Text('Enter Name Here'), sg.InputText()])],
            [self.c([sg.Checkbox('Coughness', default=False)])],
            [self.c([sg.Checkbox('Heaviness', default=False)])],
            [self.c([sg.Checkbox('Tiredness', default=False)])],
            [self.c([sg.Checkbox('Any lost of Taste? Smell?', default=False)])],
            [self.c([sg.Checkbox('Do you have any vaccines? ', default=False)])],
            [self.c([sg.Checkbox('Did you have Covid in the last 3 months? ', default=False)])],

            [sg.Button('Ok')]]
        self.window = sg.Window('Window Title', self.layout, size=(800, 300), resizable=True, finalize=True)

    def send_data(self):

        data = self.events[0] + "\t" + str('Most Likely' if self.total > 4 else 'Not Likely')
        reply = self.net.send(data)
        return reply

    @staticmethod
    def parse_data(data):
        try:
            d = data.split(":")[1].split(",")
            return int(d[0]), int(d[1])
        except:
            return 0, 0

    def transferVals(self):
        self.total = 0
        self.total += self.changing(1, 2)
        self.total += self.changing(2, 3)
        self.total += self.changing(3, 5)
        self.total += self.changing(4, 4)
        self.total += self.changing(5, -3)
        self.total += self.changing(6, -2)

        self.send_data()

    def play(self):
        sg.theme('Darkgrey3')
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
                sys.exit()

            self.events = list(values.values())
            if event == "Ok": self.transferVals()
            print(self.net.recieve(self.net.client))
        self.window.close()
