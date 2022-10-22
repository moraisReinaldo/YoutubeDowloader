import pytube 
import PySimpleGUI as sg

class Tela:
    def __init__(self):
        l = [
            [sg.Text('link'), sg.Input(key='li')],
            [sg.Button('Dowload')],
            [sg.Output(size=(50,1))]
        ]
        
        self.j = sg.Window('Dowloader').layout(l)
        
    def Iniciar(self):
        while True:
            self.button, self.values = self.j.Read()
            
            link = self.values['li']
            yt = pytube.YouTube(link)
            yt.streams.first().download()
            print(f'Baixado {link}')

tela =  Tela()
tela.Iniciar()





