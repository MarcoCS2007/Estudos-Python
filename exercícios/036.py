v=float(input('Qual o valor da casa?'))
s=float(input('Qual o valor do seu salário mensal?'))
p=float(input('Em quanto anos você pretende pagar?'))
if v/p<30*s/100*12:
    print(f'O valor da prestação é {v/p}R$ por ano, ou {v/p/12} por mês!')
else:
    print('Seu imprestimo foi recusado!')
