n=int(input('Digite um número'))
t=0
for c in range(1, n+1):
    if n%c==0:
        t+=1
        print(f'\033[1;31m{c}', end=', ')
    else:
        print(f'\033[1;33m{c}', end=', ')
if t>2:
    print(f'\n\033[mO número {n} foi dividido {t} vezes. Logo não é primo')
elif t==2:
    print(f'\n\033[mO número {n} foi dividido {t} vezes. Logo é primo')