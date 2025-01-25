from molde import ContaBancaria

p1 = ContaBancaria(4190, 250, 'Carlos Luiz de Azevedo')
p1.depositar(300)
p1.sacar(1000)
p1.sacar(500)
print(p1.saldo)