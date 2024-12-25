cont=0
soma=0
resp=''
while resp!='n':
    s=int(input('Digite um valor'))
    maior = menor = s
    if s>maior:
        maior=s
    elif s<menor:
        menor=s
    soma+=s
    cont+=1
    resp=input('Deseja continuar?\n[S/N]').lower()
print(f'Você digitou {cont} valores\n'
      f'A média dos valores foram {soma/cont}\n'
      f'O maior Valor foi {maior} e o menor valor foi {menor}')