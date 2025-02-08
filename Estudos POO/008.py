from molde import Produto

p1 = Produto('  CanETa', 'padsp1dsa5,50')
print (p1.nome, p1.preco)
print (p1.desconto(10))