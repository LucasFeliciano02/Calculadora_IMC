from tkinter import *
from tkinter import ttk
from tkinter import messagebox


cor0 = '#ffffff'  # branca
cor1 = '#444466'  # azul preto
cor2 = '#4065a1'  # azul


janela = Tk()
janela.title('Calculador de IMC')
# janela.geometry('295x230')
janela.configure(bg='white')
janela.resizable(width=FALSE, height=FALSE)
janela.iconbitmap('imc.ico')  # icon do app


style = ttk.Style(janela)
style.theme_use('clam')


# ------- Funções --------

def calcular():
    try:
        peso = float(entry_peso.get())  # * a entry.get recebe as informações, processa e envia para uma label['text'] vazia que é onde aparecera o resultado da conta
        altura = float(entry_altura.get().replace(',', '.'))  # * recebe numa entry os valores e envia numa label o resultado 

        imc = peso / (altura ** 2)
 
        resultado = imc
    
        if resultado <= 18.5:
            label_imc_texto['text'] = 'Seu IMC é:  Abaixo do peso'
        elif 18.5 <= resultado <= 24.99:
            label_imc_texto['text'] = 'Seu IMC é:  Normal'
        elif 25 <= resultado <= 29.99:
            label_imc_texto['text'] = 'Seu IMC é:  Sobrepeso'
        elif 30 <= resultado <= 34.99:
            label_imc_texto['text'] = 'Seu IMC é:  Obesidade Grau 1'
        elif 35 <= resultado <= 39.99:
            label_imc_texto['text'] = 'Seu IMC é:  Obesidade grau 2'
        elif resultado >= 40:
            label_imc_texto['text'] = 'Seu IMC é:  Obesidade morbida'

        entry_peso.delete(0, "end")
        entry_altura.delete(0, "end")
        
    except:
        messagebox.showinfo(
            'Atenção!', 'Preencha todos os campos com seus respectivos atributos.\n')
        entry_peso.delete(0, "end")
        entry_altura.delete(0, "end")
        return

    
    label_resultado['text'] = '{:.{}f}'.format(resultado, 2).replace(',', '.')  # conta: vai no quadrado azul o imc, conforme as numeros enviados nas entrys altura e peso
    
    
# ------- Frames cima e baixo --------

frame_cima = Frame(janela, width=325, height=50, bg=cor0,
                   padx=0, pady=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=295, height=180,
                    bg=cor0, padx=0, pady=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)


# ------- Configurando Label do frame_cima --------

app_nome = Label(frame_cima, text='Calculadora de IMC', width=23, height=1,
                 padx=0, relief='flat', font='Ivy 16 bold', anchor='center', bg=cor0, fg=cor1)
app_nome.place(x=11, y=1)

app_linha = Label(frame_cima, text='', width=400, height=1, padx=0,
                  relief='flat', font='Ivy 1', anchor='center', bg=cor2, fg=cor1)
app_linha.place(x=0, y=35)


# ------- Configurando Labels e Entrys do frame baixo --------

label_peso = Label(janela, text='  Insira seu peso:', height=1, padx=0,
                   relief='flat', font='Ivy 11 bold', anchor='center', bg=cor0, fg=cor1)
label_peso.place(x=2, y=65)

entry_peso = Entry(janela, width=5, relief='solid',
                   font='Ivy 10 bold', justify='center')
entry_peso.place(x=150, y=67)



label_altura = Label(janela, text=' Insira altura em M:', height=1, padx=0,
                     relief='flat', font='Ivy 11 bold', anchor='center', bg=cor0, fg=cor1)
label_altura.place(x=2, y=110)


#*
def format_imc(event=None):
    text = entry_altura.get().replace(".", "").replace("-", "")[:4]
    new_text = ""

    if event.keysym.lower() == "backspace": return
    
    for index in range(len(text)):
        
        if not text[index] in "0123456789": continue
        if index in [0, 1]: new_text += text[index] + ","
        else: new_text += text[index]

    entry_altura.delete(0, "end")
    entry_altura.insert(0, new_text)


entry_altura = Entry(janela, width=5, relief='solid',
                     font='Ivy 10 bold', justify='center')
entry_altura.place(x=150, y=112)
entry_altura.bind("<KeyRelease>", format_imc)


# ------- Quadrado Resultado do calculo do IMC --------

label_resultado = Label(frame_baixo, text='---', width=5, height=1, padx=5,
                        pady=13, relief='flat', font='Ivy 24 bold', anchor='center', bg=cor2, fg=cor0)
label_resultado.place(x=206, y=16)


# ------- Label "Seu IMC é: " que fica debaixo das entrys --------

label_imc_texto = Label(frame_baixo, text='', width=37, height=1, padx=0, pady=12,
                        relief='flat', font='Ivy 11 bold', anchor='center', bg=cor0, fg=cor1)
label_imc_texto.place(x=0, y=90)


# ------- Botao --------

label_calcular = Button(janela, command=calcular, text='Calcular', relief=RAISED,
                        width=30, overrelief=RIDGE, font='Ivy 12 bold', bg='#355ba6', fg='white')
label_calcular.place(x=7.3, y=190)


# * Centralizando o arquivo


# Dimensoes da janela
largura = 325
altura = 230

# Resolução do nosso sistema
largura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenwidth()
# print(largura_screen, altura_screen)  # para saber as dimensoes do monitor


# Posição da janela
posx = largura_screen/2 - largura/1.8
posy = altura_screen/5 - altura/5

# Definir a geometria
janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))


janela.mainloop()
