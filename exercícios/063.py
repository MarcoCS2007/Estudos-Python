print(11*'--')
print('SEQUENCIA DE FIBONACCI')
print(11*'--')
qt=int(input('Quantos termos você deseja mostrar?'))
v1=0
v2=1
cont=0
print (v1, end= ' -> ')
while cont<=qt:
    print( v2, end=' -> ')
    v3=v1+v2
    print (v3, end= ' -> ')
    v1 += v2
    v2 += v3
    cont+=1
print('Fim')