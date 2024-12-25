d = int (input ('Quantos dias o carro foi alugado?'))
km = float (input ('Quantos km foram rodados?'))
vp = 60 * d + 0.15 * km
print (f'Alugando por {d} dias e dirigindo por {km} o carro irá custar {vp:.2f}R$')