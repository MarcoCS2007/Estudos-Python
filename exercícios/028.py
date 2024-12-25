from random import randint
nc= randint(0, 5)
print ('Escolhi um número entre 0 e 5, adivinhe o número e ganhe um prêmio!')
np=int(input('escreva o número escolhido'))
import time
print ('prossessando...')
time.sleep(3)
if nc==np:
    print (f'Parabéns, realmente foi o {nc} , ganhou uma tarde com o bolsonaro!!')
else:
    print (f'Você errou, foi o {nc} vai comer picanha assada com o Lule.')