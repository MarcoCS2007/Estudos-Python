from random import randint
from time import sleep
print(15*'-=','\nBEM VINDO A CENTRAL DE JOGOS\n',15*'-=')
for c in range(1000):
    ej=int(input('\nEscolha o jogo\n[ 1 ] JOKENPO\n[ 2 ] PAR OU IMPAR'))
    if ej==1:
        jogar = int(input('Voce foi desafiado a um JOKENPO!\nDeseja participar?\n[ 1 ] SIM\n[ 2 ] NÃO\n'))
        if jogar == 1:
            print('Certo! Vamos lá!\n')
            for c in range(100):
                c1 = ('PEDRA', 'PAPEL', 'TESOURA')
                j = int(input('Opções'
                              '\n[ 1 ] PEDRA'
                              '\n[ 2 ] PAPEL'
                              '\n[ 3 ] TESOURA\nQual sua jogada?'))
                p = randint(0, 2)
                pc = c1[p]
                p1 = c1[j - 1]
                sleep(1)
                print('JO')
                sleep(1)
                print('KEN')
                sleep(1)
                print('PO')
                sleep(1)
                print(15 * '-=')
                print(f'Você escolheu {p1}\nO computador escolheu {pc}')
                print(15 * '-=')
                if j - 1 == 0:
                    if p == 0:
                        print('EMPATE')
                    elif p == 1:
                        print('Você PERDEU!')
                    elif p == 2:
                        print('Você VENCEU!!')
                elif j - 1 == 1:
                    if p == 0:
                        print('Você VENCEU!!')
                    elif p == 1:
                        print('EMPATE')
                    elif p == 2:
                        print('Você PERDEU!')
                elif j - 1 == 2:
                    if p == 0:
                        print('Você PERDEU!')
                    elif p == 1:
                        print('Você VENCEU!!')
                    elif p == 2:
                        print('EMPATE')
                jono = int(input('Deseja jogar novamente?\n[ 1 ] SIM\n[ 2 ] NÃO\n'))
                if jono == 1:
                    print('Certo! Vamos lá!')
                elif jono == 2:
                    print('Desafio encerrado!')
                    break
        elif jogar == 2:
            print('\nDesafio encerrado!')
    elif ej ==2:
        for c in range(100):
            c1 = ('PAR', 'IMPAR')
            poi = int(input('[ 1 ] PAR\n[ 2 ] IMPAR\nVocê foi desafiado a um par ou impar. Qual sua escolha?'))
            pcn = randint(0, 1000)
            print(f'Sua escolha foi {c1[poi - 1]}')
            jn = int(input('Escolha um número inteiro e teste sua sorte!'))
            if poi == 1:
                if (pcn + jn) % 2 == 0:
                    print(f'Você VENCEU!!\nO número escolhido pelo computador foi {pcn}!\n{pcn} + {jn} = {pcn + jn}')
                else:
                    print(f'Você PERDEU!!\nO número escolhido pelo computador foi {pcn}!\n{pcn} + {jn} = {pcn + jn}')
            if poi == 2:
                if (pcn + jn) % 2 == 0:
                    print(f'Você PERDEU!!\nO número escolhido pelo computador foi {pcn}!\n{pcn} + {jn} = {pcn + jn}')
                else:
                    print(f'Você VENCEU!!\nO número escolhido pelo computador foi {pcn}!\n{pcn} + {jn} = {pcn + jn}')
            djn = int(input('\n[ 1 ] SIM\n[ 2 ] NÃO\nDeseja jogar novamente?'))
            if djn == 1:
                print('Certo! Que comecem os jogos!')
            elif djn == 2:
                break
        print('Desafio encerrado! Obrigado por participar!')