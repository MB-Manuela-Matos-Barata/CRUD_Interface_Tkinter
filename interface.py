import tkinter as tk
from tkinter import messagebox
import database

# Conectar/criar o banco
database.conectar()

# Funções para botões
def adicionar_livro():
    database.inserir(titulo.get(), autor.get(), ano.get(), isbn.get())
    listar_livros()
    limpar_campos()

def listar_livros():
    lista.delete(0, tk.END)
    for livro in database.ver():
        lista.insert(tk.END, livro)

def selecionar_livro(event):
    global livro_selecionado
    index = lista.curselection()
    if index:
        livro_selecionado = lista.get(index[0])
        limpar_campos()
        titulo.insert(0, livro_selecionado[1])
        autor.insert(0, livro_selecionado[2])
        ano.insert(0, livro_selecionado[3])
        isbn.insert(0, livro_selecionado[4])

def atualizar_livro():
    if livro_selecionado:
        database.atualizar(livro_selecionado[0], titulo.get(), autor.get(), ano.get(), isbn.get())
        listar_livros()
        limpar_campos()

def deletar_livro():
    if livro_selecionado:
        database.deletar(livro_selecionado[0])
        listar_livros()
        limpar_campos()

def limpar_campos():
    titulo.delete(0, tk.END)
    autor.delete(0, tk.END)
    ano.delete(0, tk.END)
    isbn.delete(0, tk.END)

# Janela principal
janela = tk.Tk()
janela.title("Cadastro de Livros")

# Labels e Entradas
tk.Label(janela, text="Título").grid(row=0, column=0)
tk.Label(janela, text="Autor").grid(row=0, column=2)
tk.Label(janela, text="Ano").grid(row=1, column=0)
tk.Label(janela, text="ISBN").grid(row=1, column=2)

titulo = tk.Entry(janela)
titulo.grid(row=0, column=1)

autor = tk.Entry(janela)
autor.grid(row=0, column=3)

ano = tk.Entry(janela)
ano.grid(row=1, column=1)

isbn = tk.Entry(janela)
isbn.grid(row=1, column=3)

# Lista de livros
lista = tk.Listbox(janela, height=10, width=50)
lista.grid(row=2, column=0, columnspan=4, padx=10, pady=10)
lista.bind('<<ListboxSelect>>', selecionar_livro)

# Botões
tk.Button(janela, text="Adicionar", width=12, command=adicionar_livro).grid(row=3, column=0)
tk.Button(janela, text="Atualizar", width=12, command=atualizar_livro).grid(row=3, column=1)
tk.Button(janela, text="Deletar", width=12, command=deletar_livro).grid(row=3, column=2)
tk.Button(janela, text="Listar", width=12, command=listar_livros).grid(row=3, column=3)

listar_livros()  # Atualiza lista ao abrir
janela.mainloop()
