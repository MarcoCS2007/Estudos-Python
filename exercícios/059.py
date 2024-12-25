v=0
while v!=5:
    v1=int(input('Digite um valor'))
    v2=int(input('Digite um valor'))
    v=int(input('O que você deseja fazer?\n'
                '[ 1 ] Somar\n'
                '[ 2 ] Multiplicar\n'
                '[ 3 ] Maior\n'
                '[ 4 ] Digitar novos números\n'
                '[ 5 ] Sair do programa\n'))
    if v==1:
        print(v1+v2)
    elif v==2:
        print(v1*v2)
    elif v==3:
        if v1<v2:
            print(f'{v1}<{v2}')
        elif v1>v2:
            print(f'{v1}>{v2}')
        elif v1==v2:
            print(f'{v1}={v2}')
    elif v==4:
        print('')
    elif v==5:
        print('')
    else:
        print('Opção não reconhecida')
print('Adeus')