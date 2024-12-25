from idlelib.colorizer import color_config
s=float(input('Qual o valor do seu salário?'))
if s<=1250:
    print(f'O aumento do seu salário será de {s*(15/100)}R$')
if s>1250:
    print(f'Seu aumento será de {s*(10/100)}R$')

