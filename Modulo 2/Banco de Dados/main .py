import sqlite3

banco = sqlite3.connect('biblioteca.db')

cursor = banco.cursor()

import sqlite3

# Conecta (ou cria) o banco de dados chamado alunos.db
banco = sqlite3.connect('biblioteca.db')

# Cria um cursor para executar comandos SQL
cursor = banco.cursor()

#  Criando a tabela Alunos
# cursor.execute("CREATE TABLE Alunos (nome TEXT,idade INTEGER,RA TEXT, Q_livros INTEGER)")
# cursor.execute("CREATE TABLE Emprestimos (Data_de_expedição data ,Data_de_recebimento data )")
# cursor.execute("CREATE TABLE livros (titulo text, autor text, ano integer)")
# cursor.execute("CREATE TABLE Gêneros (nome text, descrição text)")
# cursor.execute("CREATE TABLE Autores (nome TEXT,nacionalidade TEXT,data_nascimento DATE)")


# Inserindo dados na tabela
# cursor.execute("INSERT INTO Alunos VALUES ('Pedro', 15, '12345678', '2')")
# cursor.execute("INSERT INTO Emprestimos VALUES ('2023-06-01', '2023-06-15')")
# cursor.execute("INSERT INTO Livros VALUES ('O Senhor dos Anéis', 'J.R.R Tolkien', 1954)")
# cursor.execute("INSERT INTO Gêneros VALUES ('Fantasia', 'Histórias que envolvem elementos mágicos e sobrenaturais')")
cursor.execute("INSERT INTO Autores VALUES ('J.R.R Tolkien', 'Britânica', '1892-01-03')")

# 3 Deletar informação
# cursor.execute("DELETE FROM Alunos WHERE nome ='Pedro'")

# Atualizar informação
# cursor.execute("UPDATE Alunos SET nome='Gustavo' WHERE nome='Stefany'")

# 5️⃣ Confirmar as mudanças no banco
banco.commit()

# 6️⃣ Mostrar todas as informações
# cursor.execute("SELECT * FROM Alunos")
# print(cursor.fetchall())

# Fechar conexão
banco.close()

# cursor.execute("UPDATE ")




