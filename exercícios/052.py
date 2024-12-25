f=input('Digite uma frase!').strip().upper()
junto=f.replace(' ', '')
nf=len(junto)
s=''
for c in range(nf-1,-1,-1):
    s+=junto[c]
if s==junto:
    print('isso é um palindromo')
else:
    print('isso não é um palindromo')

