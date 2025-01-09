'''a distribuição de poisson qualcula a probabilidade que um evento ocorra com base em uma media de eventos
, delimitados por tempo,espaço ou volume'''
'''qual a probabilidade de um atendente que recebe 8 chamadas em 10 min, receber 10 chamadas?'''

def poisson(media,possibilidade):
    import math
    c = ((2.71828)**(-media)*(media**possibilidade))/(math.factorial(possibilidade))
    print(f'a probabilidade é de {c*100}%')

poisson(8,10)

poisson(288,270)