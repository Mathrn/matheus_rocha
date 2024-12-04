######CONTROLE

from Database import Database

class Usuario:
    def __init__(self) -> None:
        self.nome = None
        self.cpf = None
        self.email = None
        self.senha = None
        self.banco = Database()

# classe de produto
class Produto:
    def __init__(self,id_prod,nome,descricao,marca,modelo,preco,qtd,cor,peso):
        self.id_prod = id_prod
        self.nome = nome
        self.descricao = descricao
        self.marca = marca
        self.modelo = modelo
        self.preco =preco
        self.qtd =qtd
        self.cor = cor
        self.peso =peso
        self.banco =Database()


# cadastra usuario 

    def cadastrar(self):
        tupla = (self.nome,self.cpf,self.email,self.senha)
        res = self.banco.insert(tupla)
        return res
    
# cadastra produto

    def cadastrarprod(self):
        tupla = (self.id_prod,self.nome,self.descricao,self.marca,self.modelo,self.preco,self.qtd,self.cor,self.peso)
        res = self.banco.insertprod(tupla)
        return res

# lista usuarios 
    def listar(self):
        res = self.banco.select()
        return res

# lista produtos

    def listarprod(self):
        res = self.banco.selectprod()
        return res
    
# lista usuarios  por id
    def lista_por_id(self,id):
        res = self.banco.select_by_id(id)
        return list(res)

# lista produtos por id 

    def listaprod_por_id(self,id):
        res = self.banco.selectprod_by_id(id)
        return list(res)

# atualiza usuario

    def atualizar(self,lista):
        res = self.banco.update(lista)
        return res
    
# atualiza produto

    def atualizarprod(self,lista):
        res = self.banco.updateprod(lista)
        return res
    
# exclui usuarios 

    def excluir(self,id):
        res = self.banco.delete(id)
        return res
    
# exclui produtos

    def excluir(self,id):
        res = self.banco.deleteprod(id)
        return res
    

# adicionamos 1 produto na tabela !!

prod1 = Produto(1,'playtation5','playtation top','playstation','PRO',5000,4,'BRANCO',0.900)
prod1 = Produto(1, 'playstation5', 'playstation top', 'playstation', 'PRO', 5000, 4, 'BRANCO', 0.900)
prod2 = Produto(2, 'xbox series x', 'console da microsoft', 'xbox', 'Series X', 4500, 3, 'PRETO', 1.0)
prod3 = Produto(3, 'nintendo switch', 'console híbrido', 'nintendo', 'OLED', 3000, 5, 'BRANCO', 0.500)
prod4 = Produto(4, 'iphone 14', 'smartphone da apple', 'apple', '14 Pro Max', 8000, 2, 'DOURADO', 0.300)
prod5 = Produto(5, 'samsung galaxy s23', 'smartphone android', 'samsung', 'S23 Ultra', 7000, 3, 'PRATA', 0.350)
prod6 = Produto(6, 'smart tv lg', 'TV 4K UHD', 'LG', '55UP7750', 2500, 7, 'PRETO', 10.0)
prod7 = Produto(7, 'notebook dell', 'notebook para trabalho', 'DELL', 'Inspiron 15', 3500, 5, 'CINZA', 1.8)
prod8 = Produto(8, 'cadeira gamer', 'cadeira ergonômica', 'ThunderX3', 'BC3', 1200, 6, 'AZUL', 15.0)
prod9 = Produto(9, 'monitor ultrawide', 'monitor para trabalho', 'Samsung', 'Odyssey G5', 1800, 4, 'PRETO', 5.5)
prod10 = Produto(10, 'headset gamer', 'headset com som 7.1', 'HyperX', 'Cloud Alpha', 600, 10, 'PRETO/VERMELHO', 0.400)

prod1.cadastrarprod()
prod2.cadastrarprod()
prod3.cadastrarprod()
prod4.cadastrarprod()
prod5.cadastrarprod()
prod6.cadastrarprod()
prod7.cadastrarprod()
prod8.cadastrarprod()
prod9.cadastrarprod()
prod10.cadastrarprod()
