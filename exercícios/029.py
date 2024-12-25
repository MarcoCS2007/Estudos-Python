v=float(input('Qual a velocidade do carro?'))
if v>80:
    print (f'O carro utrapassou a velocidade permitida em {v-80}km/h')
    print (f'O valor da multa a ser pago será de:\n{7*(v-80)}R$')
else:
    print ('\nVocê estava dentro do limite de velocidade!\n\nTENHA UM BOM DIA!!!')