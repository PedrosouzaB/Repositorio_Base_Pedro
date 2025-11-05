import sqlite3

# Conecta (ou cria) o banco de dados chamado alunos.db

banco = sqlite3.connect('fabrica_programadores.db')

# Cria um cursor para executar comandos SQL

cursor = banco.cursor()


# Criando a tabela Cursos
# cursor.execute ("CREATE TABLE Alunos (id integer primary key autoincrement,nome text,idade integer,cidade text)")
# cursor.execute("CREATE TABLE Cursos (id integer primary key autoincrement,nome text, carga_horaria REAL,  duração text)")
# cursor.execute("CREATE TABLE Professores (id integer primary key autoincrement,nome text, especialidade text)")
# cursor.execute("CREATE TABLE Matriculas (id INTEGER PRIMARY KEY AUTOINCREMENT,id_aluno INTEGER,id_curso INTEGER,data TEXT, FOREIGN KEY (id_aluno) REFERENCES Alunos(id),FOREIGN KEY (id_curso) REFERENCES Cursos(id))")

#Inserindo dados na tabela
# cursor.execute ("INSERT INTO Alunos (nome, idade,cidade) VALUES ('ARTHUR FELIX CAETANO COSTA', 16,'Barra Mansa')")
# cursor.execute ("INSERT INTO Alunos (nome, idade,cidade) VALUES ('DAVI ANTENOR VIEIRA MACHADO', 15,'Barueri')")
# cursor.execute ("INSERT INTO Alunos (nome, idade,cidade) VALUES ('EZEQUIEL MANTUANO SOUSA DOS SANTOS', 16,'Barueri')")
# cursor.execute ("INSERT INTO Alunos (nome, idade,cidade) VALUES ('GUSTAVO SOUZA SANTOS', 17,'Santana de Parnaíba')")
# cursor.execute ("INSERT INTO Alunos (nome, idade,cidade) VALUES ('ISÁAC DE OLIVEIRA SALES', 15,'Barueri')")
# cursor.execute ("INSERT INTO Alunos (nome, idade,cidade) VALUES ('ISABELLE EDUARDA DOS SANTOS CUNHA', 15,'Itapevi')")
# cursor.execute ("INSERT INTO Alunos (nome, idade,cidade) VALUES ('ISABELLE LUISA MARTINS DE ARRUDA ', 15,'Itapevi')")
# cursor.execute ("INSERT INTO Alunos (nome, idade,cidade) VALUES ('JOSÉ BENEDITO ALVES DOS SANTOS', 15,'Osasco')")
# cursor.execute ("INSERT INTO Alunos (nome, idade,cidade) VALUES ('JUAN PEDRO FREITAS DA SILVA', 15,'Carapicuíba')")
# cursor.execute ("INSERT INTO Alunos (nome, idade,cidade) VALUES ('KAUA VINICIUS CASTRO ARAUJO', 15,' Pernambuco')")
# cursor.execute ("INSERT INTO Alunos (nome, idade,cidade) VALUES ('KETHLEEN VITÓRIA PEREIRA', 15,'Barueri')")
# cursor.execute ("INSERT INTO Alunos (nome, idade,cidade) VALUES ('PEDRO HENRIQUE BRUNNER SOUZA', 15,'Barueri')")
# cursor.execute ("INSERT INTO Alunos (nome, idade,cidade) VALUES ('REBECA VIEIRA CASTELO', 15,'Itapevi')")
# cursor.execute ("INSERT INTO Alunos (nome, idade,cidade) VALUES ('ROBERTA MIKAELLY', 15,'Guarulhos')")
# cursor.execute ("INSERT INTO Alunos (nome, idade,cidade) VALUES ('VITORIA ALVES MARQUES DA SILVA', 15,'Barueri')")
# cursor.execute ("INSERT INTO Alunos (nome, idade,cidade) VALUES ('GUSTAVO ALESSANDRO BATISTA SOBRAL', 16,'Barueri')")
# cursor.execute ("INSERT INTO Alunos (nome, idade,cidade) VALUES ('Maisa Alves de Souza', 15,'Santo Amaro')")

#Tabela Cursos
# cursor.execute("INSERT INTO Cursos (nome, carga_horaria, duração) VALUES ('Python para Iniciantes', 30.5, '2 meses')")
# cursor.execute("INSERT INTO Cursos (nome, carga_horaria, duração) VALUES ('Python Intermediário', 60.0, '3 meses')")
# cursor.execute("INSERT INTO Cursos (nome, carga_horaria, duração) VALUES ('Python Avançado', 80.0, '4 meses')")
# cursor.execute("INSERT INTO Cursos (nome, carga_horaria, duração) VALUES ('Desenvolvimento Web', 28.0, '5 meses')")
# cursor.execute("INSERT INTO Cursos (nome, carga_horaria, duração) VALUES ('Data Science', 120.0, '6 meses')")
# cursor.execute("INSERT INTO Cursos (nome, carga_horaria, duração) VALUES ('Desenvolvimento de Jogos', 90.0, '4 meses')")
# cursor.execute("INSERT INTO Cursos (nome, carga_horaria, duração) VALUES ('Inteligência Artificial', 39.0, '5 meses')")

#Tabela professores 
# cursor.execute("INSERT INTO Professores (nome, especialidade) VALUES ('Ricardão','Pyton')")
# cursor.execute("INSERT INTO Professores (nome, especialidade) VALUES ('Ana Paula','Python intermediario')")
# cursor.execute("INSERT INTO Professores (nome, especialidade) VALUES ('Gabriel','Python avançado')")
# cursor.execute("INSERT INTO Professores (nome, especialidade) VALUES ('Jubileu','Desenvolvimento Web')")
# cursor.execute("INSERT INTO Professores (nome, especialidade) VALUES ('Creuza','Data Science')")
# cursor.execute("INSERT INTO Professores (nome, especialidade) VALUES ('Pedrinho','Desenvolvimento de Jogos')")
# cursor.execute("INSERT INTO Professores (nome, especialidade) VALUES ('Lucas','Inteligência Artificial')")

#Tabela Matriculas
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, data) VALUES (1, 1, '2024-01-15')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, data) VALUES (2, 2, '2024-02-20')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, data) VALUES (3, 3, '2024-03-10')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, data) VALUES (4, 4, '2024-01-25')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, data) VALUES (5, 5, '2024-02-15')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, data) VALUES (6, 6, '2024-03-05')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, data) VALUES (7, 7, '2024-01-30')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, data) VALUES (8, 1, '2024-02-10')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, data) VALUES (9, 2, '2024-03-15')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, data) VALUES (10, 3, '2024-01-20')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, data) VALUES (11, 4, '2024-02-25')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, data) VALUES (12, 5, '2024-03-10')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, data) VALUES (13, 6, '2024-01-18')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, data) VALUES (14, 7, '2024-02-22')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, data) VALUES (15, 1, '2024-03-08')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, data) VALUES (16, 2, '2024-01-28')")
# cursor.execute("INSERT INTO Matriculas (id_aluno, id_curso, data) VALUES (17, 3, '2024-02-12')")


#Deletar informação
# cursor.execute("DELETE FROM Alunos WHERE nome ='Maisa Alves de Souza'")

#Selecionar informação
# cursor.execute("SELECT * FROM Alunos")
# cursor.execute("SELECT carga_horaria FROM Cursos WHERE carga_horaria >= 40 order by carga_horaria DESC"))
# cursor.execute("SELECT Alunos.nome, Cursos.nome, Matriculas.data FROM Matriculas JOIN Alunos ON Matriculas.id_aluno = Alunos.id JOIN Cursos ON Matriculas.id_curso = Cursos.id")
cursor.execute("SELECT FROM Alunos MATRICULAS WHERE id_aluno = 1")

#Atualizar informação

print(cursor.fetchall())




# Confirmar as mudanças no banco
banco.commit()
