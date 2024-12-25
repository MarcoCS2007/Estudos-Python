n=int(input('Difite um número que você deseja converter?'))
e=int(input('Para qual base deseja converter?\n1-Binário\n2-Octal\n3-Hexadecimal\n'))
if e==1:
    print(f'O valor convertido é:\n {bin(n)[2::]}')
elif e==2:
    print(f'O valor convertido é:\n {oct(n)[2::]}')
elif e==3:
    print(f'O valor convertido é\n {hex(n)[2::]}')
else:
    print('Valor não reconhecido. Escolha uma das alternativas.')
