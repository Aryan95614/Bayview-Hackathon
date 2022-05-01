import PySimpleGUI as sg
from multiprocessing import Process
from Hackathon.body import *



def process1():
    window = Window()
    window.play()


if __name__ == "__main__":
    sg.theme('Darkgrey3')
    p = Process(target=process1(), args=('bob',))
    p.start()
