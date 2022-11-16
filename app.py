import tkinter.messagebox as MessageBox
from tkinter import *
from PIL import Image, ImageTk
import os



c=os.path.dirname(__file__)
criaPasta = 'Dados'
if criaPasta == '':
    os.mkdir('Dados')
else:
    print('A pasta "Dados" ja existe')
    pass

nomeArquivo="seusdados.txt"

#----- INICIO ------#

def vali():
    if box1.get() and box2.get() != "":
        arquivo=open(nomeArquivo,"a")
        arquivo.write("Nome..:%s" % box1.get())
        arquivo.write("\nIdade.:%s anos" % box2.get())
        arquivo.write("\n\n")
        box1.delete(0, END)
        box2.delete(0, END)
        arquivo.close()
    else:
        print('Preencha os dois campos!')

def opendados():
    os.startfile('seusdados.txt')

#----- FIM FUNCAO ------#

#-------- INICIO APP --------#

app = Tk()
app.geometry("400x420+0+0")
app.title("DADOS PESSOAIS")
app.configure(background="#272631")

    
title = Label(app, text="Insira seus dados",font=("Arial",18), bg="#272631", fg="white")
title.place(x=115, y=50)

texto1 = Label(app, text="Digite seu nome abaixo:", fg="white" ,bg="#272631", font=("Arial", 12))
texto1.place(x=70, y=115)

box1 = Entry(app, width=24,font=("Arial", 15),fg="#373541",highlightbackground = "#565460", highlightthickness = 2, bd=0)
box1.place(x=70, y = 140)


texto2 = Label(app, text="Digite sua idade abaixo:", fg="white" ,bg="#272631", font=("Arial", 13))
texto2.place(x=70, y=185)

box2 = Entry(app, width=24,font=("Arial", 15), fg="#373541",highlightbackground = "#565460", highlightthickness = 2, bd=0)
box2.place(x=70, y = 210)


botao = Button(app, text="Enviar dados", width=20, command=vali, font=("Arial",12), bg="#373541", fg="white")
botao.place(x=110, y=270)

text3 = Label(app, text="Clique no botão abaixo para abrir os dados", font=("Arial",11),bg="#272631", fg="white")
text3.place(x=50, y=310)

openb = Button(app, text="Abrir Dados",command=opendados, font=("Arial",12), bg="#373541", fg="white", width=15)
openb.place(x=135, y=350)


app.mainloop()

#--------- FIM APP --------#

