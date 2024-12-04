#nome produto,descricao,marca,modelo,preco,qtd,cor,peso
from Database import Database


class Produto:
    def __init__(self) -> None:
        self.nome = None
        self.descricao = None
        self.marca = None 
        self.modelo = None
        self.preco = None
        self.qtd =None
        self.cor = None
        self.peso =None
        self.banco = Database()

        
    def cadastrar_prod(self,tupla):
        
        tupla = (self.nome,self.descricao,self.marca,self.modelo,self.preco,self.qtd,self.cor,self.peso)
        res = self.banco.insertprod(tupla)
        return res

    def listar(self):
        res = self.banco.select()
        return res
    
    def lista_por_id(self,id):
        res = self.banco.select_by_id(id)
        return list(res)

    def atualizar(self,lista):
        res = self.banco.update(lista)
        return res
    
    def excluir(self,id):
        res = self.banco.delete(id)
        return res


prod1 =Produto()
teste = (1,'playtation5','playtation top','playstation','PRO',5000,4,'BRANCO',0.900)
prod1.cadastrar_prod(teste)

#1,'playtation5','playtation top','playstation','PRO',5000,4,'BRANCO',0.900