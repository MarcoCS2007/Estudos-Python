vezes=0
vi = int(input('Qual o valor inicial da PA?'))
vr = int(input('Qual a razão da PA?'))
while vezes<11:
    print (vi, end=' -> ')
    vi+=vr
    vezes+=1
print ('Fim')