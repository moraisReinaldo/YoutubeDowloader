from curses import keyname
import pytube 
import PySimpleGUI as sg

class Tela:
    def __init__(self):
        l = [
            [sg.Text('link'), sg.Input(), keyname = 'li']
            [sg.Button()]
        ]
        
        j = sg.Window('Dowloader').layout(l)
        
        self.button, self.values = j.Read()
        
    def Iniciar(self):
        link = self.values['li']
        yt = pytube.YouTube(link)
        yt.streams.first().download()
        print("Baixado", link)






