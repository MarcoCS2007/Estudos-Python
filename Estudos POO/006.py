from molde import pessoa_update

p1 = pessoa_update.get_ano_nascimento('Marco', 'Chaves', 2007)
print(p1.idade)
print(p1.nome_completo())
