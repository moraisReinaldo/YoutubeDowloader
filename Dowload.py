import pytube 
import PySimpleGUI as sg

class Tela:
    def __init__(self):
        l = [
            [sg.Text('link'), sg.Input(key='li')],
            [sg.Text('Pasta para salvar'), sg.Input(key='pa')],
            [sg.Button('Dowload')],
            [sg.Output(size=(50,1))]
        ]
        
        self.j = sg.Window('Dowloader').layout(l)
        
    def Iniciar(self):
        while True:
            self.button, self.values = self.j.Read()

            link = self.values['li']
            path = self.values['pa']
            
            yt = pytube.YouTube(link)
            
            yv = yt.streams.get_highest_resolution()
            
            print('Baixando...')
            
            yv.download(path)

            print(f'Baixado {link}')

tela =  Tela()
tela.Iniciar()





