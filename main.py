from turtle import Turtle, Screen
import pandas as pd

''' Screen '''

screen = Screen()
screen.title('US States Game - by Marco Aurélio Menezes (100 Dias)')
imagem = 'blank_states_img.gif'
screen.addshape(imagem)
turtle = Turtle()
turtle.shape(imagem)

''' Pandas '''
estados = pd.read_csv('50_states.csv')

''' Funções '''


class NameState(Turtle):
    def __init__(self, estado, x, y):
        super().__init__()
        self.estado = estado
        self.penup()
        self.goto(x, -y)
        self.color('Black')
        self.write(self.estado, font=('Arial', 12, 'bold'))
        self.hideturtle()
        # self.acertos = 0
        # self.erros = 0



acertos = 0

def ver_se_tem_estado(estado):
    apareceu = 0
    for row in estados.state:
        if row == estado:
            global acertos
            acertos += 1
            apareceu = 1
            print('O estado  está na lista!')
            print(estados.loc[estados.state == estado])
            informacoes = (estados.loc[estados.state == estado])
            name = str(estado)
            print(name)
            x = int(informacoes.x)
            print(x)
            y = int(informacoes.y)
            print(y)
            name_state = NameState(name, x, y)


    if apareceu == 0:
        print('O estado não está na lista!')


''' Main '''
game_on = True
#
while game_on:

    answer_state = screen.textinput(title=f'{acertos}/50 Acerte o nome dos Estados',prompt= 'Qual estado você sabe o nome?')
    # answer_state = 'Alaska'
    ver_se_tem_estado(answer_state)


screen.mainloop()
