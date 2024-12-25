r=''
s=''
while r!='V':
    r=str(input('Qual seu sexo? [M/F]')).upper()
    if r=='M':
        s='M'
        r='V'
    elif r=='F':
        s='F'
        r='V'
print(f'Obrigado Sexo registrado {s}!')
