import mysql.connector

class Database:
    def __init__(self,banco='crud_py'):
        self.banco = banco
        self.conn = None

    def connect(self):
        self.conn = mysql.connector.connect(host='localhost',database='crud_py',user='root',password='')
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            print("Conectado com sucesso!!!")
            print("UUUHHHHUUULLLLLLL \\o/")
        else:
            print("Error")


# insere um usuario
    def insert(self,tupla):
        self.connect()
        try:
            self.cursor.execute('INSERT INTO usuario (nome,cpf,email,senha) VALUES (%s,%s,%s,%s)',tupla)
            self.conn.commit()
            return True

        except Exception as erro:
            return erro
        
        finally:
            self.close_connection()


#insere um produto
    def insertprod(self,tupla):
        self.connect()
        try:
            self.cursor.execute('INSERT INTO produto (id_produto,nome,descricao,marca,modelo,preco,qtd,cor,peso) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);',tupla)
            self.conn.commit()
            return True

        except Exception as erro:
            return erro
        
        finally:
            self.close_connection()


# seleciona usuario
    def select(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM usuario")
            dados = self.cursor.fetchall()
            return dados

        except Exception as erro:
            print(erro)

        finally:
            self.close_connection()


#seleciona produto
    def selectprod(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM produto")
            dados = self.cursor.fetchall()
            return dados

        except Exception as erro:
            print(erro)

        finally:
            self.close_connection()


#seleciona o usuario pelo id

    def select_by_id(self,id):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM usuario WHERE id = {id}")
            dados = self.cursor.fetchone()
            return dados

        except Exception as erro:
            print(erro)

        finally:
            self.close_connection()
#seleciona o produto pelo id

    def selectprod_by_id(self,id):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM produto WHERE id_produto = {id}")
            dados = self.cursor.fetchone()
            return dados

        except Exception as erro:
            print(erro)

        finally:
            self.close_connection()


#atualiza o banco de usuarios


    def update(self,lista):
        self.connect()
        print("lista que chegou no banco: ",lista)
        try:
            self.cursor.execute(f"""
                                UPDATE usuario 
                                SET nome = '{lista[1]}',
                                cpf = '{lista[2]}',
                                email = '{lista[3]}',
                                senha = '{lista[4]}'
                                WHERE id = {lista[0]}
                                """)
            
            self.conn.commit()
            return True
        
        except Exception as erro:
            print(erro)

        finally:
            self.close_connection()
        
# atualiza banco de produtos

    def updateprod(self,lista):
        self.connect()
        print("lista que chegou no banco: ",lista)
        try:
            self.cursor.execute(f"""
                                UPDATE produto 
                                SET nome = '{lista[1]}',
                                descricao = '{lista[2]}',
                                marca = '{lista[3]}',
                                modelo = '{lista[4]}',
                                preco = '{lista[5]},
                                qtd ='{lista[6]}',  
                                                                                        WHERE id_produto = {lista[0]}
                                """)
            
            self.conn.commit()
            return True
        
        except Exception as erro:
            print(erro)

        finally:
            self.close_connection()

# exclui usuarios

    def delete(self,id):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM usuario WHERE id = {id}")
            self.conn.commit()
            return True
        
        except Exception as erro:
            print(erro)

        finally:
            self.close_connection()

# exclui produtos

    def deleteprod(self,id):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM produto WHERE id_produto= {id}")
            self.conn.commit()
            return True
        
        except Exception as erro:
            print(erro)

        finally:
            self.close_connection()

    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Conexao encerrada com sucesso!!!!")
    

if __name__ == "__main__":
    banco = Database()
    banco.select_by_id(3)