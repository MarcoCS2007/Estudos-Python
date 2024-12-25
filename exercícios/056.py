hv=''
ih=0
im=0
si=0
for c in range(0,4):
    print(10 * '-=')
    sx=int(input('Qual seu sexo? \n[ 1 ] Homem \n[ 2 ] Mulher\n'))
    idade=int(input('Quantos anos tens?'))
    nome=input('Qual seu nome?')
    print(10*'-=')
    si+=idade
    if c==0 and sx==1:
        hv=nome
        ih+=idade
    elif sx==1 and ih<idade:
        ih=idade
        hv=nome
    if idade<20 and sx==2:
        im+=1
print(f'O Homem mais velho é {hv}\n'
      f'Tem {im} mulheres menores de 20 anos\n'
      f'A idade média do grupo é {si/4}')