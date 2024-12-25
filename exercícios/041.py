from datetime import date
a=int(input('Qual o ano de nascimento do atleta?'))
i=date.today().year-a
print(f'O atleta tem {i} anos.')
if i<=9:
    print('Categoria MIRIM')
elif 9<i<=14:
    print('Categoria INFANTIL')
elif 14<i<=19:
    print('Categoria JUNIOR')
elif 19<i<=25:
    print('Categoria SÊNIOR')
elif i>25:
    print('Categoria MASTER')