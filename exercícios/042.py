t1=float(input('Qual o lado 1 do triangulo?'))
t2=float(input('Qual o lado 2 do triangulo?'))
t3=float(input('Qual o lado 3 do triangulo?'))
if not t1+t2>t3 or not t3+t2>t1 or not t1+t3>t2:
    print('impossivel formar triangulos com essas medidas.')
elif t1==t2==t3:
    print('O triangulo será EQUILÁTERO')
elif t1==t2!=t3 or t3==t2!=t1 or t1==t3!=t2:
    print('O triangulo será ISÓSCELES')
elif t1!=t2!=t3:
    print('O triangulo será ESCALENO')