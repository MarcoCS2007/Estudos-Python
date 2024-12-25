a=float(input('Qual sua altura(cm)?'))
p=float(input('Qual o seu peso(kg)?'))
imc=p/((a/100)**2)
if imc<18.5:
    print('Você está abaixo do peso')
elif imc<=25:
    print('Peso ideal')
elif imc<=30:
    print('Você está com sobrepeso!')
elif imc<=40:
    print('Você tem a massa de um hipopotamo')
else:
    print('Calma Thaiso Carlo')