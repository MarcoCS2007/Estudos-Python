n=int(input('Escreva um número para obter sua tabuada até o 100'))
print(15*'=')
for c in range(0, 101):
    print(f'{n} X {c} = {n*c}')
print(15*'=')