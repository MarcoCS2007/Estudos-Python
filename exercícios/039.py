from datetime import date
n=int(input('Qual seu ano de Nascimento?'))
hj=date.today().year
if hj-n<18:
    print(f'Você ainda tem {18-(hj-n)} anos para se alistar!')
elif hj-n==18:
    print('Você deve se alistar imediatamente')
else:
    print(f'Você está atrasado! Já devia ter se alistado a {hj-n} anos!!')