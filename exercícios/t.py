from random import randint
for c in range (5):
    c = ('PAR', 'IMPAR')
    poi=int(input('[ 1 ] PAR\n[ 2 ] IMPAR\nVocê foi desafiado a um par ou impar. Qual sua escolha?'))
    pcn=randint(0, 1000)
    print(f'Sua escolha foi {c[poi-1]}')
    jn=int(input('Escolha um número inteiro e teste sua sorte!'))
    if poi==1:
        if (pcn+jn)%2==0:
            print (f'Você VENCEU!!\nO número escolhido pelo computador foi {pcn}!\n{pcn} + {jn} = {pcn+jn}')
        else:
            print(f'Você PERDEU!!\nO número escolhido pelo computador foi {pcn}!\n{pcn} + {jn} = {pcn + jn}')
    if poi==2:
        if (pcn+jn)%2==0:
            print (f'Você PERDEU!!\nO número escolhido pelo computador foi {pcn}!\n{pcn} + {jn} = {pcn+jn}')
        else:
            print(f'Você VENCEU!!\nO número escolhido pelo computador foi {pcn}!\n{pcn} + {jn} = {pcn + jn}')
    djn=int(input('\n[ 1 ] SIM\n[ 2 ] NÃO\nDeseja jogar novamente?'))
    if djn == 1:
        print('Certo! Que comecem os jogos!')
    elif djn == 2:
        break
print('Desafio encerrado! Obrigado por participar!')

