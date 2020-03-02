import funcoes
from tkinter import *


def take():
    secao = text_area.get()
    if funcoes.check_paths(funcoes.list_way(secao), 't')[1]:
        feedback['text'] = funcoes.check_paths(funcoes.list_way(secao), 't')[0]
        funcoes.creates_paths(funcoes.list_way(secao), 't')
        feedback['text'] = funcoes.copy_refs(funcoes.list_way(secao), 't')

    else:
        feedback['text'] = funcoes.check_paths(funcoes.list_way(secao), 't')[0]


def drop():
    secao = text_area.get()
    if funcoes.check_paths(funcoes.list_way(secao), 'd')[1]:
        feedback['text'] = funcoes.check_paths(funcoes.list_way(secao), 'd')[0]
        funcoes.creates_paths(funcoes.list_way(secao), 'd')
        feedback['text'] = funcoes.copy_refs(funcoes.list_way(secao), 'd')
    else:
        feedback['text'] = funcoes.check_paths(funcoes.list_way(secao), 'd')[0]


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
