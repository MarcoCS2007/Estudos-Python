from random import randint
pc=randint(0,10)
j=11
t=0
while j!=pc:
    j=int(input('Digite um número de 0 a 10 e teste sua sorte!'))
 #   print(f'Valor do pc {pc}')
    if j!=pc:
        print ('Valor icorreto!')
    t+=1
print(f'Acertou em {t} tentativas')