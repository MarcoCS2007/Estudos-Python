v=float(input('Qual o valor da compras?'))
p=int(input('Qual o método de pagamento?\n[ 1 ] à vista dinheiro/cheque\n[ 2 ] à vista no cartão\n[ 3 ] em até 2x no cartão\n[ 4 ] 3x ou mais no cartão\n'))
if p==1:
    print(f'O valor cobrado será de {(90*v)/100}R$')
elif p==2:
    print(f'O valor cobrado será de {(95*v)/100}R$')
elif p==3:
    print(f'O valor será cobrado em duas parcelas de {v/2}R$\nValor total a ser pagp{v}R$')
elif p==4:
    p4=int(input('Em quantas parcelas?'))
    print(f'O valor será cobrado em {p4} parcelas de {((120*v)/100)/p4}R$\nValor total a ser pago {(120*v)/100}R$')