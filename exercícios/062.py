vezes=0
vi = int(input('Qual o valor inicial da PA?'))
vr = int(input('Qual a razão da PA?'))
while vezes <= 10:
    print (vi, end=' -> ')
    vi+=vr
    vezes+=1
print ('Pausa')
vf =- 1
while vf != 0:
    v2 = vf = int(input('Quantos termos você quer mostrar a mais?'))
    while vezes <= v2+10:
        print(vi, end=' -> ')
        vi += vr
        vezes += 1
    print('Pausa')
print ('fim')