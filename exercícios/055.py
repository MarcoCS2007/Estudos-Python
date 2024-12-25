ma=0
me=0
for c in range(0, 5):
    p=float(input('Qual o seu peso?'))
    if c==0:
        ma=p
        me=p
    else:
        if p>ma:
            ma=p
        elif p<me:
            me=p
print(f'A pessoa mais pesada pesa {ma}kg e a mais leve pesa {me}kg')