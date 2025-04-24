import sqlite3

def conectar():
    conn = sqlite3.connect("livros.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano TEXT,
            isbn TEXT
        )
    ''')
    conn.commit()
    conn.close()

def inserir(titulo, autor, ano, isbn):
    conn = sqlite3.connect("livros.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO livro (titulo, autor, ano, isbn) VALUES (?, ?, ?, ?)", (titulo, autor, ano, isbn))
    conn.commit()
    conn.close()

def ver():
    conn = sqlite3.connect("livros.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livro")
    dados = cursor.fetchall()
    conn.close()
    return dados

def atualizar(id, titulo, autor, ano, isbn):
    conn = sqlite3.connect("livros.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE livro SET titulo=?, autor=?, ano=?, isbn=? WHERE id=?", (titulo, autor, ano, isbn, id))
    conn.commit()
    conn.close()

def deletar(id):
    conn = sqlite3.connect("livros.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM livro WHERE id=?", (id,))
    conn.commit()
    conn.close()
