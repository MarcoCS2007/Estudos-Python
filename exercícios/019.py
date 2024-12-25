from random import choice
a1 = input ('Nome do primeiro aluno')
a2 = input ('nome do segundo aluno')
a3 = input ('nome do terceiro aluno')
a4 = input ('nome do quarto aluno')
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print (f'O aluno escolhido foi {escolhido}')