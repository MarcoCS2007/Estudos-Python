km=float(input('Qual a distância até o destino?'))
if km<=200:
    print(f'O valor cobrado será {km*0.50:.2f}R$')
if km>200:
    print(f'O valor cobrado será {km*0.45:.2f}R$')
print('Esperamos que tenha uma boa viagem!')