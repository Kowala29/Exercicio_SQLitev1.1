import sqlite3

class Crud:

    def __init__(self):
        self.conexao = sqlite3.connect("alunos.sqlite")
        self.cursor  = self.conexao.cursor()

    def fechar(self):
        self.conexao.close()
        print("fechou")

    def criar(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS alunos(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            disciplina TEXT NOT NULL,
            idade INTEGER NOT NULL
            );
        '''
        self.cursor.execute(sql)
        print("tabela criada")

    def ler(self):
        sql = '''
            SELECT * FROM alunos
        '''
        resultado = self.cursor.execute(sql)
        return resultado.fetchall()
    
    def inserir(self, campos, nome, disciplina, idade):
        valores = '('
        resultado = '('
        for campo in campos:
            resultado += f"{campo}, "
            valores += f"?, "
        resultado = resultado[:-2]+ ")"
        valores = valores[:-2] + ")"
        sql = f'''
            INSERT INTO alunos {resultado}
            VALUES{valores}
        '''
        self.cursor.execute(sql, (nome, disciplina, idade))
        self.conexao.commit()
        return "Salvo com Sucesso!"
    
    def alterar(self, nome, disciplina, idade, id):
        sql = '''
            UPDATE SET alunos
            SET nome = ?, disciplina = ?, idade = ?,
            WHERE id = ?;
        '''

        self.cursor.execute(sql, [nome, disciplina, idade, id])
        self.conexao.commit()

    def deletar(self, coluna, id):
        sql = f'''
            DELETE FROM alunos
            WHERE {coluna} = ?;
        '''
        self.cursor.execute(sql, (coluna, id))
        self.conexao.commit()

campos = ("nome", "disciplina", "idade")
#dados = ["Eduardo", "prog1", 18]

nome = input("Entre com seu nome: ")
disciplina = input("Entre com a Disciplina: ")
idade = int(input("Entre com sua idade: "))
id = int(input("entre com o ID: "))
coluna = input("Entre com a coluna desejada: ")

#print(dados1)
a = Crud()
#a.criar()
#a.inserir(campos, nome, disciplina, idade)
#print(a.ler())
a.alterar(nome, disciplina, idade, id)
#a.deletar(coluna, id)

a.fechar()