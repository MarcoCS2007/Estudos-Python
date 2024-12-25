npe=('zero', 'um', 'dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    n = int(input('digite um número entre 0 e 20\n'))
    if 20>=n>=0:
        print(f'O número digitado foi {npe[n]}')
        break
    else:
        print('Número não reconhecido.\nTente novamente')