from datetime import date
hj=date.today().year
menor=0
maior=0
for c in range(0, 7):
    i=int(input('Qual a data de nascimento do elemento?'))
    if hj-i<18:
        menor+=1
    else:
        maior+=1
print(f'Na lista existem {menor} pessoas menores de idade e {maior} pessoas maiores de idade.')
