import funcoes
from tkinter import *


def take():
    feedback['text'] = 'Pegando...'
    secao = text_area.get()
    funcoes.criaCaminho(funcoes.listaCaminho(secao))
    feedback['text'] = funcoes.copiaRefs(funcoes.listaCaminho(secao))
    # feedback['text'] = 'Tarefa finalizada'


def drop():
    feedback['text'] = 'Droping!'


janela = Tk()
janela.geometry('530x110')
janela.title('Gerenciador de Pastas')
janela.wm_iconbitmap('favicon.ico')

container1 = Frame(janela)
container1.pack()

container2 = Frame(janela)
container2.pack()

container3 = Frame(janela, borderwidth=5)
container3.pack()

container4 = Frame(janela)
container4.pack()

enunciated = Label(container1, text='Cole os caminhos', font=('Arial', '11', 'bold'), fg='#353535')
enunciated.pack()

text_area = Entry(container2, width='70', bg='#353535', fg='#f2f2f2', font=('Arial', '9', 'bold'))
text_area.pack()

take_button = Button(container3, text='Pegar', font=('Arial', '9', 'bold'), border=3, padx=102, command=take,
                     fg='#353535')
take_button.pack(side=LEFT)

drop_button = Button(container3, text='Jogar', font=('Arial', '9', 'bold'), border=3, padx=102, command=drop,
                     fg='#353535')
drop_button.pack(side=LEFT)

feedback = Label(container4, text='', font=('Arial', '11', 'bold'), fg='#353535')
feedback.pack()

janela.mainloop()
