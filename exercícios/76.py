menu=(input('Qual o nome do material?'),
      float(input('Qual o preco?')),
      input('Qual o nome do material?'),
      float(input('Qual o preco?')),
      input('Qual o nome do material?'),
      float(input('Qual o preco?')),
      input('Qual o nome do material?'),
      float(input('Qual o preco?')))
for c in range(0,len(menu)):
    if c%2==0:
        print (f'{menu[c]:.<30}', end='')
    else:
        print (f'{menu[c]}R$')
